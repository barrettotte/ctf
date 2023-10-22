import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Base85 {
    private static final long Power4 = 52200625L;

    private static final long Power3 = 614125L;

    private static final long Power2 = 7225L;

    private static Encoder RFC1924ENCODER;

    private static Encoder Z85ENCODER;

    private static Encoder ASCII85ENCODER;

    private static Decoder RFC1924DECODER;

    private static Decoder Z85DECODER;

    private static Decoder ASCII85DECODER;

    public static abstract class Encoder {
        public int calcEncodedLength(String data) {
            return calcEncodedLength(data.getBytes(StandardCharsets.UTF_8));
        }

        public int calcEncodedLength(byte[] data) {
            return calcEncodedLength(data, 0, data.length);
        }

        public int calcEncodedLength(byte[] data, int offset, int length) {
            if (offset < 0 || length < 0)
                throw new IllegalArgumentException("Offset and length must not be negative");
            return (int)Math.ceil(length * 1.25D);
        }

        public final String encode(String data) {
            return encodeToString(data.getBytes(StandardCharsets.UTF_8));
        }

        public final String encodeToString(byte[] data) {
            return new String(encode(data), StandardCharsets.US_ASCII);
        }

        public final String encodeToString(byte[] data, int offset, int length) {
            return new String(encode(data, offset, length), StandardCharsets.US_ASCII);
        }

        public final byte[] encode(byte[] data) {
            return encode(data, 0, data.length);
        }

        public final byte[] encode(byte[] data, int offset, int length) {
            byte[] out = new byte[calcEncodedLength(data, offset, length)];
            int len = _encode(data, offset, length, out, 0);
            if (out.length == len)
                return out;
            return Arrays.copyOf(out, len);
        }

        public final int encode(byte[] data, int offset, int length, byte[] out, int out_offset) {
            int size = calcEncodedLength(data, offset, length);
            return _encode(data, offset, length, out, out_offset);
        }

        public byte[] encodeBlockReverse(byte[] data) {
            int size = Math.max(0, (int)Math.ceil(data.length * 1.25D));
            byte[] result = new byte[size];
            encodeBlockReverse(data, 0, data.length, result, 0);
            return result;
        }

        public int encodeBlockReverse(byte[] data, int offset, int length, byte[] out, int out_offset) {
            int size = (int)Math.ceil(length * 1.25D);
            if (offset != 0 || length != data.length)
                data = Arrays.copyOfRange(data, offset, offset + length);
            BigInteger sum = new BigInteger(1, data), b85 = BigInteger.valueOf(85L);
            byte[] map = getEncodeMap();
            for (int i = size + out_offset - 1; i >= out_offset; i--) {
                BigInteger[] mod = sum.divideAndRemainder(b85);
                out[i] = map[mod[1].intValue()];
                sum = mod[0];
            }
            return size;
        }

        protected int _encodeDangling(byte[] encodeMap, byte[] out, int wi, ByteBuffer buffer, int leftover) {
            long sum = buffer.getInt(0) & 0xFFFFFFFFL;
            out[wi] = encodeMap[(int)(sum / 52200625L)];
            sum %= 52200625L;
            out[wi + 1] = encodeMap[(int)(sum / 614125L)];
            sum %= 614125L;
            if (leftover >= 2) {
                out[wi + 2] = encodeMap[(int)(sum / 7225L)];
                sum %= 7225L;
                if (leftover >= 3)
                    out[wi + 3] = encodeMap[(int)(sum / 85L)];
            }
            return leftover + 1;
        }

        protected int _encode(byte[] in, int ri, int rlen, byte[] out, int wi) {
            int wo = wi;
            ByteBuffer buffer = ByteBuffer.allocate(4);
            byte[] buf = buffer.array(), encodeMap = getEncodeMap();
            for (int loop = rlen / 4; loop > 0; loop--, ri += 4) {
                System.arraycopy(in, ri, buf, 0, 4);
                wi = _writeData(buffer.getInt(0) & 0xFFFFFFFFL, encodeMap, out, wi);
            }
            int leftover = rlen % 4;
            if (leftover == 0)
                return wi - wo;
            buffer.putInt(0, 0);
            System.arraycopy(in, ri, buf, 0, leftover);
            return wi - wo + _encodeDangling(encodeMap, out, wi, buffer, leftover);
        }

        protected int _writeData(long sum, byte[] map, byte[] out, int wi) {
            out[wi] = map[(int)(sum / 52200625L)];
            sum %= 52200625L;
            out[wi + 1] = map[(int)(sum / 614125L)];
            sum %= 614125L;
            out[wi + 2] = map[(int)(sum / 7225L)];
            sum %= 7225L;
            out[wi + 3] = map[(int)(sum / 85L)];
            out[wi + 4] = map[(int)(sum % 85L)];
            return wi + 5;
        }

        protected abstract byte[] getEncodeMap();

        public String getCharset() {
            return new String(getEncodeMap(), StandardCharsets.US_ASCII);
        }
    }

    public static class Rfc1924Encoder extends Encoder {
        private static final byte[] ENCODE_MAP = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~".getBytes(StandardCharsets.US_ASCII);

        protected byte[] getEncodeMap() {
            return ENCODE_MAP;
        }
    }

    public static class IPv6Encoder extends Encoder {
        private static final byte[] ENCODE_MAP = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~".getBytes(StandardCharsets.US_ASCII);

        protected byte[] getEncodeMap() {
            return ENCODE_MAP;
        }
    }

    public static class Z85Encoder extends Encoder {
        private static final byte[] ENCODE_MAP = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#".getBytes(StandardCharsets.US_ASCII);

        protected byte[] getEncodeMap() {
            return ENCODE_MAP;
        }
    }

    public static class Ascii85Encoder extends Encoder {
        private static final byte[] ENCODE_MAP = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstu".getBytes(StandardCharsets.US_ASCII);

        protected byte[] getEncodeMap() {
            return ENCODE_MAP;
        }

        public int calcEncodedLength(byte[] data, int offset, int length) {
            int result = super.calcEncodedLength(data, offset, length);
            if (this.useZ || this.useY) {
                ByteBuffer buffer = ByteBuffer.wrap(data);
                for (int i = offset, len = offset + length - 4; i <= len; i += 4) {
                    if (this.useZ && data[i] == 0) {
                        if (buffer.getInt(i) == 0)
                            result -= 4;
                    } else if (this.useY && data[i] == 32 &&
                            buffer.getInt(i) == 538976288) {
                        result -= 4;
                    }
                }
            }
            return result;
        }

        private boolean useZ = true;

        private boolean useY = true;

        private final ReadWriteLock lock = new ReentrantReadWriteLock(true);

        public void setZeroCompression(boolean compress) {
            this.lock.writeLock().lock();
            try {
                this.useZ = compress;
            } finally {
                this.lock.writeLock().unlock();
            }
        }

        public boolean getZeroCompression() {
            this.lock.readLock().lock();
            try {
                return this.useZ;
            } finally {
                this.lock.readLock().unlock();
            }
        }

        public void setSpaceCompression(boolean compress) {
            this.lock.writeLock().lock();
            try {
                this.useY = compress;
            } finally {
                this.lock.writeLock().unlock();
            }
        }

        public boolean getSpaceCompression() {
            this.lock.readLock().lock();
            try {
                return this.useY;
            } finally {
                this.lock.readLock().unlock();
            }
        }

        protected int _encode(byte[] in, int ri, int rlen, byte[] out, int wi) {
            this.lock.readLock().lock();
            try {
                return super._encode(in, ri, rlen, out, wi);
            } finally {
                this.lock.readLock().unlock();
            }
        }

        protected int _writeData(long sum, byte[] map, byte[] out, int wi) {
            if (this.useZ && sum == 0L) {
                out[wi++] = 122;
            } else if (this.useY && sum == 538976288L) {
                out[wi++] = 121;
            } else {
                return super._writeData(sum, map, out, wi);
            }
            return wi;
        }
    }

    public static abstract class Decoder {
        public int calcDecodedLength(String data) {
            return calcDecodedLength(data.getBytes(StandardCharsets.US_ASCII));
        }

        public int calcDecodedLength(byte[] data) {
            return calcDecodedLength(data, 0, data.length);
        }

        public int calcDecodedLength(byte[] data, int offset, int length) {
            if (length % 5 == 1)
                throw new IllegalArgumentException("" + length + " is not a valid Base85/" + length + " data length.");
            return (int)(length * 0.8D);
        }

        public final String decode(String data) {
            return new String(decode(data.getBytes(StandardCharsets.US_ASCII)), StandardCharsets.UTF_8);
        }

        public final byte[] decode(byte[] data) {
            return decode(data, 0, data.length);
        }

        public final byte[] decodeToBytes(String data) {
            return decode(data.getBytes(StandardCharsets.US_ASCII));
        }

        public final byte[] decode(byte[] data, int offset, int length) {
            byte[] result = new byte[calcDecodedLength(data, offset, length)];
            try {
                int len = _decode(data, offset, length, result, 0);
                if (result.length != len)
                    return Arrays.copyOf(result, len);
            } catch (ArrayIndexOutOfBoundsException ex) {
                throwMalformed(ex);
            }
            return result;
        }

        public final int decode(byte[] data, int offset, int length, byte[] out, int out_offset) {
            int size = calcDecodedLength(data, offset, length);
            try {
                _decode(data, offset, length, out, out_offset);
            } catch (ArrayIndexOutOfBoundsException ex) {
                throwMalformed(ex);
            }
            return size;
        }

        public byte[] decodeBlockReverse(byte[] data) {
            int size = Math.max(0, (int)Math.ceil(data.length * 0.8D));
            byte[] result = new byte[size];
            decodeBlockReverse(data, 0, data.length, result, 0);
            return result;
        }

        public int decodeBlockReverse(byte[] data, int offset, int length, byte[] out, int out_offset) {
            int size = (int)Math.ceil(length * 0.8D);
            BigInteger sum = BigInteger.ZERO, b85 = BigInteger.valueOf(85L);
            byte[] map = getDecodeMap();
            try {
                for (int i = offset, len = offset + length; i < len; i++)
                    sum = sum.multiply(b85).add(BigInteger.valueOf(map[data[i]]));
            } catch (ArrayIndexOutOfBoundsException ex) {
                throwMalformed(ex);
            }
            System.arraycopy(sum.toByteArray(), 0, out, out_offset, size);
            return size;
        }

        public boolean test(String data) {
            return test(data.getBytes(StandardCharsets.US_ASCII));
        }

        public boolean test(byte[] data) {
            return test(data, 0, data.length);
        }

        public boolean test(byte[] encoded_data, int offset, int length) {
            return _test(encoded_data, offset, length);
        }

        protected boolean _test(byte[] data, int offset, int length) {
            byte[] valids = getDecodeMap();
            try {
                for (int i = offset, len = offset + length; i < len; i++) {
                    byte e = data[i];
                    if (valids[e] < 0)
                        return false;
                }
                calcDecodedLength(data, offset, length);
            } catch (ArrayIndexOutOfBoundsException|IllegalArgumentException ex) {
                return false;
            }
            return true;
        }

        protected RuntimeException throwMalformed(Exception ex) {
            throw new IllegalArgumentException("Malformed Base85/" + getName() + " data", ex);
        }

        protected int _decodeDangling(byte[] decodeMap, byte[] in, int ri, ByteBuffer buffer, int leftover) {
            if (leftover == 1)
                throwMalformed(null);
            long sum = decodeMap[in[ri]] * 52200625L + decodeMap[in[ri + 1]] * 614125L + 85L;
            if (leftover >= 3) {
                sum += decodeMap[in[ri + 2]] * 7225L;
                if (leftover >= 4) {
                    sum += (decodeMap[in[ri + 3]] * 85);
                } else {
                    sum += 7225L;
                }
            } else {
                sum += 621350L;
            }
            buffer.putInt(0, (int)sum);
            return leftover - 1;
        }

        protected int _decode(byte[] in, int ri, int rlen, byte[] out, int wi) {
            int wo = wi;
            ByteBuffer buffer = ByteBuffer.allocate(4);
            byte[] buf = buffer.array(), decodeMap = getDecodeMap();
            for (int loop = rlen / 5; loop > 0; loop--, wi += 4, ri += 5) {
                _putData(buffer, decodeMap, in, ri);
                System.arraycopy(buf, 0, out, wi, 4);
            }
            int leftover = rlen % 5;
            if (leftover == 0)
                return wi - wo;
            leftover = _decodeDangling(decodeMap, in, ri, buffer, leftover);
            System.arraycopy(buf, 0, out, wi, leftover);
            return wi - wo + leftover;
        }

        protected void _putData(ByteBuffer buffer, byte[] map, byte[] in, int ri) {
            buffer.putInt(0, (int)(map[in[ri]] * 52200625L + map[in[ri + 1]] * 614125L + map[in[ri + 2]] * 7225L + (map[in[ri + 3]] * 85) + map[in[ri + 4]]));
        }

        protected abstract byte[] getDecodeMap();

        protected abstract String getName();
    }

    public static class Rfc1924Decoder extends Decoder {
        private static final byte[] DECODE_MAP = new byte[127];

        static {
            Base85.buildDecodeMap(Base85.Rfc1924Encoder.ENCODE_MAP, DECODE_MAP);
        }

        protected String getName() {
            return "RFC1924";
        }

        protected byte[] getDecodeMap() {
            return DECODE_MAP;
        }
    }

    public static class Z85Decoder extends Decoder {
        private static final byte[] DECODE_MAP = new byte[127];

        static {
            Base85.buildDecodeMap(Base85.Z85Encoder.ENCODE_MAP, DECODE_MAP);
        }

        protected String getName() {
            return "Z85";
        }

        protected byte[] getDecodeMap() {
            return DECODE_MAP;
        }
    }

    private static class Ascii85Decoder extends Decoder {
        private static final byte[] zeros = new byte[] { 0, 0, 0, 0 };

        private static final byte[] spaces = new byte[] { 32, 32, 32, 32 };

        public int calcDecodedLength(byte[] encoded_data, int offset, int length) {
            int deflated = length, len = offset + length;
            int i;
            for (i = offset; i < len; i += 5) {
                if (encoded_data[i] == 122 || encoded_data[i] == 121) {
                    deflated += 4;
                    i -= 4;
                }
            }
            if (i != len) {
                i -= 5;
                while (i < len && (encoded_data[i] == 122 || encoded_data[i] == 121)) {
                    deflated += 4;
                    i -= 4;
                }
            }
            return super.calcDecodedLength(null, 0, deflated);
        }

        public boolean test(byte[] encoded_data, int offset, int length) {
            try {
                int deviation = 0;
                for (int i = offset, len = offset + length; i < len; i++) {
                    byte e = encoded_data[i];
                    if (DECODE_MAP[e] < 0) {
                        if ((deviation + i - offset) % 5 != 0 || (e != 122 && e != 121))
                            return false;
                        deviation += 4;
                    }
                }
                super.calcDecodedLength(null, 0, length + deviation);
            } catch (ArrayIndexOutOfBoundsException|IllegalArgumentException ignored) {
                return false;
            }
            return true;
        }

        private static final byte[] DECODE_MAP = new byte[127];

        static {
            Base85.buildDecodeMap(Base85.Ascii85Encoder.ENCODE_MAP, DECODE_MAP);
        }

        protected String getName() {
            return "Ascii85";
        }

        protected byte[] getDecodeMap() {
            return DECODE_MAP;
        }

        protected int _decode(byte[] in, int ri, int rlen, byte[] out, int wi) {
            int re = ri + rlen, wo = wi;
            ByteBuffer buffer = ByteBuffer.allocate(4);
            byte[] buf = buffer.array(), decodeMap = getDecodeMap();
            for (int max = ri + rlen, max2 = max - 4; ri < max; ) {
                while (ri < max && (in[ri] == 122 || in[ri] == 121)) {
                    byte[] src = null;
                    switch (in[ri++]) {
                        case 122:
                            src = zeros;
                            break;
                        case 121:
                            src = spaces;
                            break;
                    }
                    System.arraycopy(src, 0, out, wi, 4);
                    wi += 4;
                }
                if (ri < max2) {
                    _putData(buffer, decodeMap, in, ri);
                    ri += 5;
                    System.arraycopy(buf, 0, out, wi, 4);
                    wi += 4;
                }
            }
            if (re == ri)
                return wi - wo;
            int leftover = _decodeDangling(decodeMap, in, ri, buffer, re - ri);
            System.arraycopy(buf, 0, out, wi, leftover);
            return wi - wo + leftover;
        }
    }

    private static void buildDecodeMap(byte[] encodeMap, byte[] decodeMap) {
        Arrays.fill(decodeMap, (byte)-1);
        for (byte i = 0, len = (byte)encodeMap.length; i < len; i = (byte)(i + 1)) {
            byte b = encodeMap[i];
            decodeMap[b] = i;
        }
    }

    public static Encoder getRfc1924Encoder() {
        if (RFC1924ENCODER == null)
            RFC1924ENCODER = new Rfc1924Encoder();
        return RFC1924ENCODER;
    }

    public static Decoder getRfc1924Decoder() {
        if (RFC1924DECODER == null)
            RFC1924DECODER = new Rfc1924Decoder();
        return RFC1924DECODER;
    }

    public static Encoder getZ85Encoder() {
        if (Z85ENCODER == null)
            Z85ENCODER = new Z85Encoder();
        return Z85ENCODER;
    }

    public static Decoder getZ85Decoder() {
        if (Z85DECODER == null)
            Z85DECODER = new Z85Decoder();
        return Z85DECODER;
    }

    public static Encoder getAscii85Encoder() {
        if (ASCII85ENCODER == null)
            ASCII85ENCODER = new Ascii85Encoder();
        return ASCII85ENCODER;
    }

    public static Decoder getAscii85Decoder() {
        if (ASCII85DECODER == null)
            ASCII85DECODER = new Ascii85Decoder();
        return ASCII85DECODER;
    }

    public static void main(String[] args) {}
}
