import math
from pwn import *

context.log_level = 'DEBUG'
io = remote('147.182.225.243', 33000)

n = []
for i in range(1,500+1):
    if i % 3 == 0 and i % 7 == 0:
        n.append('TURBOTACTICAL')
    elif i % 7 == 0:
        n.append('TACTICAL')
    elif i % 3 == 0:
        n.append('TURBO')
    else:
        n.append(str(i))

solve = '[' + ', '.join(n) + ']'

print(io.recvuntil(b']').decode('utf-8'))
# io.recvlines(1)

# io.send(solve.encode('utf-8'))
io.sendline(solve.encode('utf-8'))

io.interactive()
# io.recvline()
# io.recvline()
# io.recvline()
# io.recvline()
