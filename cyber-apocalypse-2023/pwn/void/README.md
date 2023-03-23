# void

> The room goes dark and all you can see is a damaged terminal. 
> Hack into it to restore the power and find your way out.

TODO: review writeup

https://github.com/Mymaqn/HTBCA2023_Pwn_Writeups/tree/master/void

## Attempt

```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
    RUNPATH:  b'./glibc/'
```

```sh
ldd void
        # linux-vdso.so.1 (0x00007ffc3db21000)
        # libc.so.6 => ./glibc/libc.so.6 (0x00007fc1cc03d000)
        # ./glibc/ld-linux-x86-64.so.2 => /lib64/ld-linux-x86-64.so.2 (0x00007fc1cc214000)

readelf -s ./glibc/libc.so.6 | grep system
# 1430: 0000000000045e50    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5

strings -a -t x ./glibc/libc.so.6 | grep /bin/sh
# 196152 /bin/sh

ROPgadget --binary void | grep rdi
# 0x00000000004011bb : pop rdi ; ret
```

```sh
# gdb
b *vuln+30
```

ret2libc?
