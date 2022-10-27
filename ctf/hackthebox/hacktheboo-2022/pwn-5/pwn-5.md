# pwn 5

```sh
file finale
# ELF 64 LSB, dynamic, not stripped

checksec --file=finale
# no stack canary, NX enabled, no PIE

strings finale
# nothing of interest?

ltrace ./finale
# nothing

strace ./finale

readelf -a finale


# README says to avoid using libc-based techniques
```

```txt
open in Ghidra

secret phrase: s34s0nf1n4l3b00
outputs memory address?


```
