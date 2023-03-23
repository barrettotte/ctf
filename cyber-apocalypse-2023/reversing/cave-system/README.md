# cave-system

**SOLVED**

```sh
strings cave

gdb cave
info file 

set disassembly-flavor intel
layout asm
layout regs

starti
```

ghidra

```asm
lea     rsi, aHtb       ; "HTB{"
```

gigantic if statement (`cave.c`)...there's no way we're supposed to do this manually

https://www.youtube.com/watch?v=RCgEIBfnTEI

https://shivsarthak.medium.com/angr-for-ctf-automating-reversing-a-binary-d5ca574d1d0b

```sh
pip3 install angr
python3 flag.py
```

`HTB{H0p3_u_d1dn't_g3t_th15_by_h4nd,1t5_4_pr3tty_l0ng_fl4g!!!}`