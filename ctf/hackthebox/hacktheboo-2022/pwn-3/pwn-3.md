# Pwn 3 - Pumpking

```sh
file pumpking
# ELF 64 pie, dynamic link

readelf -a pumpking
# entry 0x11c0

strings pumpking
# nothing

# built docker container and ran
nc 127.0.0.1 1337
# wants a password or something

# 's' => invalid system call
# '2' => invalid system call (Open)

# flag.txt in dockerfile, need to trigger open somehow
# workdir /home/ctf => /home/ctf/flag.txt
```

```sh
# opened in ghidra
# found pumpk1ngRulez => leads to next prompt (different user?)

echo 'pumpk1ngRulez' | nc 0.0.0.0 1337 

# leads to king()

# hmm something has to be put in because otherwise program just ends?
```


```txt

read(0,&local_a8,0x95);

0x95=149

https://guyinatuxedo.github.io/6.1-mitigation_nx/index.html

ASLR, NX, and CANARY
https://github.com/slimm609/checksec.sh
```


```txt
        00101406 48 8d 85        LEA        RAX=>local_a8,[RBP + -0xa0]
                 60 ff ff ff
        0010140d ba 95 00        MOV        EDX,0x95
                 00 00
        00101412 48 89 c6        MOV        RSI,RAX
        00101415 bf 00 00        MOV        EDI,0x0
                 00 00
        0010141a e8 61 fd        CALL       <EXTERNAL>::read                                 ssize_t read(int __fd, void * __
                 ff ff


0x0a is the start of what I think should be shellcode inject
```

