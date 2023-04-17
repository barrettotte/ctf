# Pwn 2 - Entity

T -> L -> Maybe Try a Ritual

```c
static union {
    unsigned long long integer; // 64-bit
    char string[8];
} DataStore;

// ... enums

typedef struct { 
    action_t act;
    field_t field;
} menu_t;

// overflow buffer into menu ??


// DataStore in bss segment

```

```sh

# compile my own copy with debug symbols
gcc entity.c -g -o my-entity

gdb my-entity -ex 'layout src' -ex 'b 109'

# gdb
print DataStore
print &DataStore   # 0x555555558030
x/32ub &DataStore


gdb entity
info file 

set disassembly-flavor intel
layout asm
layout regs

starti

# 0x0000555555558070 .bss
# 
```

take 13371337 and reverse to bytes? (char in C = byte)


```sh
# https://nikhilh20.medium.com/format-string-exploit-ccefad8fd66b

# T->L
# "00011122233344455566677788899" 
# causes "What's this nonsense?!" (29 bytes?)
```


wrote `exploit.py` with pwntools; `cat: flag.txt: No such file or directory` ... I think its working enough?

added remote access to `exploit.py`

