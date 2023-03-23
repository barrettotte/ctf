from pwn import *

# io = process('./janken')
io = remote('167.99.200.95', 30543)

prompt = b'>>'

print(io.recvuntil(prompt))
io.sendline(b'1')

print(io.recvuntil(prompt))
for i in range(0, 101):
    io.sendline(b'rockpaperscissors')
    try:
        print(io.recvuntil(prompt))
    except EOFError:
        io.interactive()

try:
    io.recvline(20)
except EOFError:
    pass
