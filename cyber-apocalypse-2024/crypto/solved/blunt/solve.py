from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes

p = 0xdd6cc28d
g = 0x83e21c05
A = 0xcfabb6dd
B = 0xc4a21ba9
encrypted = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'

iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'

# find original a,b
# def find_private(pub):
#     i = 0
#     for x in range(1, p):
#         if i % 200_000_000 == 0:
#             print('i:', i)
#         if pow(g, x, p) == pub:
#             return x
#         i += 1
#     raise Exception(f"Private key not found for {pub}")

# a = find_private(A)
# print('Found a:', a) 
a = 2766777741

# b = find_private(B)
# print('Found b:', b)
b = 1913706799

C = pow(B, a, p)
assert C == pow(A, b, p)

h = SHA256.new()
h.update(long_to_bytes(C))
k = h.digest()[:16]

cipher = AES.new(k, AES.MODE_CBC, iv)

flag = unpad(cipher.decrypt(encrypted), 16)
print(flag.decode())

# HTB{y0u_n3ed_a_b1gGeR_w3ap0n!!}
