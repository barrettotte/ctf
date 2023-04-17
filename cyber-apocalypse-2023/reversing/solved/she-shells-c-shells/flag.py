# from pwn import *

# io = process('./shell')
# prompt = 'ctfsh-$'

# print(io.recv())
# print(f'waiting on prompt {prompt}')

# # io.sendlineafter(prompt, b'getflag')
# print(io.recv())

# payload = b'2c4ab799a3e57078936e97d9476d38bdffbb85996fe14aab74c37ba8b29fd7ecebcd63b23923e184929609c699f258facb6f6f5e1fbe2b138ea5a99993ab8f701cc0c43ea6fe933590c3c910e9'

# io.sendline(payload)
# io.interactive()


hex_t = '2c4ab799a3e57078936e97d9476d38bdffbb85996fe14aab74c37ba8b29fd7ecebcd63b23923e184929609c699f258facb6f6f5e1fbe2b138ea5a99993ab8f701cc0c43ea6fe933590c3c910e9'
hex_m1 = '6e3fc3b9d78d1558e50ffbac224d57dbdfcfedfc1c846ad81ca617c4c1bfa08587a143d4584f8da8b2f27ca3b98637dabf070a7e73df5c60aecacfb9e0deff0070b9e45fc89ab351f5aea87e8d'

t = int(hex_t, 16)
m1 = int(hex_m1, 16)

print(t)
print(m1)

xor1 = t ^ m1

hex_xor1 = hex(xor1)
print(hex_xor1)

# 0x427574207468652076616c7565206f66207468657365207368656c6c732077696c6c2066616c6c2c2064756520746f20746865206c617773206f6620737570706c7920616e642064656d616e64
# But the value of these shells will fall, due to the laws of supply and demand
