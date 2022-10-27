# pwn 4 - spooky time


```sh
file spooky_time
# ELF 64 LSB pie, dynamic, not stripped

strings spooky_time
# crtstuff.c
# completed.0
# spooky_time.c

readelf -a spooky_time
# entry point 0x1160

strace ./spooky_time
# nothing

ltrace ./spooky_time
# nothing
```

```c
char local_154[12];   // %llu  Unsigned long long
char local_148[312];  // %299s 



__isoc99_scanf("%299s", local_148)
printf(local_148)

// %p%p%p%p%p%p
// 0x10x10x7f20d942aa370x2a0x7f20d952f280
//
// GOT exploit via printf
//
// overwrite puts() with system()
// how to get system command in ?
//

```

overwrite got __stack_check_fail address to system(), completely ignore canary check?

https://libc.blukat.me/

leak canary with first printf
leak libc lib functions 
find way back to base of binary

leak canary, buffer overflow, leak GOT address
buffer overflow return to libc, call system bin/sh

https://www.youtube.com/watch?v=KgDeMJNK5BU&list=RDCMUCEeuul0q7C8Zs5C8rc4REFQ&index=6


finally got checksec working

`checksec spooky_time`

canary found, NX enable, PIE enabled, No RELRO

RELRO -> able to overwrite GT

%1 = b'0x1'
%2 = b'0x1'
%3 = b'0x7fcc4f741a37'
%4 = b'0x2a'
%5 = b'0x7fec7b4e9280'
%6 = b'0x4141414100000000'
%7 = b'0x70243725'
%8 = b'0x8000'
%9 = b'(nil)'
%10 = b'0xc0000'
%11 = b'0x2000'
%12 = b'(nil)'
%13 = b'0x40'
%14 = b'0x8'
%15 = b'0x40'
%16 = b'0x40'

https://guyinatuxedo.github.io/5.1-mitigation_aslr_pie/index.html
https://axcheron.github.io/exploit-101-format-strings/
https://ir0nstone.gitbook.io/notes/types/stack
https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html

leak pie addr, calc offset

