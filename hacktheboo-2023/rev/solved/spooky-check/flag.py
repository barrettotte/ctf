import binascii

KEY = b'SUP3RS3CR3TK3Y'

flag = []
s = 'HTB{hello}'
for i,c in enumerate(s.encode()):
    x = ((((c+24) & 255) ^ KEY[i%len(KEY)]) - 74) & 255
    flag.append(x)

flag = bytes(flag)
print(flag)                   # b'\xe9\xef\xc0V\x88\xe4m}\x8b\\'
print(binascii.hexlify(flag)) # b'e9efc05688e46d7d8b5c'

print('------------')
CHECK = bytearray(b'\xe9\xef\xc0V\x8d\x8a\x05\xbe\x8ek\xd9yX\x8b\x89\xd3\x8c\xfa\xdexu\xbe\xdf1\xde\xb6\\')
print(binascii.hexlify(CHECK)) # b'e9efc0568d8a05be8e6bd979588b89d38cfade7875bedf31deb65c'


def decode(c,i):
    return ((((c+24) & 255) ^ KEY[i%len(KEY)]) - 74) & 255

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-{}!@#$%^&*()-+='.encode()

decoded = []
for i,c in enumerate(CHECK):
    for x in alphabet:
        f = decode(x, i)
        if c == f:
            decoded.append(x)
            break

decoded = ''.join([chr(i) for i in decoded])
print('FLAG!', decoded)
