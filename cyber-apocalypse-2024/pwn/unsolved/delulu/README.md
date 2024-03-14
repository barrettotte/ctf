# delulu

HALT! Recognition protocol initiated. Please present your face for scanning.

## Solution

```sh
checksec --file=delulu
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled
# RUNPATH:  b'./glibc/'
```

```c
// main
  long in_FS_OFFSET;
  long local_48;
  long *local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_48 = 0x1337babe;
  local_40 = &local_48;
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;

  read(0,&local_38,0x1f); // 31

  printf("\n[!] Checking.. ");
  printf((char *)&local_38);

  if (local_48 == 0x1337beef) {
    delulu();
  }
  else {
    error("ALERT ALERT ALERT ALERT\n");
  }

  // ...
```

```
file delulu

layout asm
layout regs
info file

starti
b *main+12
c
```

TODO:
