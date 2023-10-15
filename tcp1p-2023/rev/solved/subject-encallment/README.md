# subject-encallment

If there's something strange. In your neighborhood. Who you gonna call?

## Solution

```sh
file chall
# chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), 
# dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d622fa9f4c0527b5ae297227883f3d5701d056d1, 
# for GNU/Linux 3.2.0, not stripped
```

0x001011a9 -> secretFunction()
0x00101ba5 -> printFlag()

b *main+29
set $rip = *printFlag

`TCP1P{here_my_number_so_call_me_maybe}`

## Alternative Solutions

Could also do this:

```sh
$ gdb chall
> break main
> r
> jump printFlag
```
