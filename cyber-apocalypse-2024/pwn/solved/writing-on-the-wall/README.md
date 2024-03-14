# writing-on-the-wall

As you approach a password-protected door, a sense of uncertainty envelops you—no clues, no hints. 
Yet, just as confusion takes hold, your gaze locks onto cryptic markings adorning the nearby wall. 
Could this be the elusive password, waiting to unveil the door's secrets?

## Solution

```sh
strings writing_on_the_wall | less
# w3tpass H

ltrace ./writing_on_the_wall
```

```
AAAABBBBCCCCDDDDEEEEFFFF, overflows BCCCCDDDDEEEEFFFF

AAAAAAAABBBBBBBBCCCCCCCC, overflows ABBBBBBBBCCCCCCCC
```

```c
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_18 = 0x2073736170743377;

  read(0,local_1e,7); // overflow

  iVar1 = strcmp(local_1e,(char *)&local_18);
  if (iVar1 == 0) {
    open_door();
  }
  else {
    error("You activated the alarm! Troops are coming your way, RUN!\n");
  }
```

```
gdb

set disassembly-flavor intel

file writing_on_the_wall
layout asm
layout regs
info file

starti
b *main+12
c
```

0x2073736170743377 -> w3tpass

HTB{3v3ryth1ng_15_r34d4bl3}

## Post-CTF

Actually the exploit could have been done by:

```py
pwn.sendlineafter(b">>", "\x00"*7)
```

The null byte comparison was the actual exploit, I found it by chance.
