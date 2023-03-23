import binascii
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64encode,b64decode

def encode(message):
    return hex(bytes_to_long(b64encode(message)))

def decode(message):
    decoded = int.from_bytes(bytes.fromhex(message), byteorder='big')
    decoded = long_to_bytes(decoded)
    decoded = b64decode(decoded)
    return decoded.decode("utf-8", errors="ignore")

def main():
    encoded = '53465243657a467558336b7764584a66616a4231636d347a655639354d48566664326b786246397a5a544e66644767784e56396c626d4d775a4446755a334e665a58597a636e6c33614756794d33303d'    
    print(f"encoded: '{encoded}'")
    flag = decode(encoded)
    print('flag =>', flag)

if __name__ == "__main__":
    main()