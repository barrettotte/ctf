# poetry


## LimFib

```
pop ecx / pop ecx / xor edx, eax /
inc ebx / nop edx / test ebx, eax /
.xadd: / nop ebx /
nop / xadd eax, ebx /
nop ecx / loop .xadd / test ebx, eax /
EOF
```

```
pop ebx / pop ecx / inc edx /
.edx: / add eax, edx /
nop / nop / nop / nop / nop / nop /
nop / nop / nop / nop / nop / nop /
xchg edx, eax / loop .edx /
```