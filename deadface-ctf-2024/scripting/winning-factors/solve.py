import math
from pwn import *

context.log_level = 'DEBUG'

io = remote('147.182.245.126', 33001)

i = 0
while i < 100:
    s = io.recvuntil(b'.').decode('utf-8')
    print(s)

    if 'Nope' in s:
        print('FAILED')
        break

    n = int(s[:-1].split(' ')[-1])
    f = math.factorial(n)
    print(f'{n}! = {f}')

    io.send_raw(str(f).encode('utf-8'))

    i += 1
