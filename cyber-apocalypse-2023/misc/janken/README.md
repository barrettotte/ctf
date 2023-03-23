# janken

**SOLVED**

```sh
strings janken
# oh rock,paper,scissors
```

opened in ghidra

```c
local_78[0] = "rock";
local_78[1] = "scissors";
local_78[2] = "paper";
local_38 = 0;
local_30 = 0;
local_28 = 0;
local_20 = 0;
local_58[0] = "paper";
local_58[1] = &DAT_0010252a;
local_58[2] = "scissors";

read(0,&local_38,0x1f) // 31 bytes
```

strstr(const char *haystack, const char *needle) function finds the first occurrence of the substring needle in the string haystack

lmao oh enter 'rockpaperscissors' and you win

`python3 flag.py`

`HTB{r0ck_p4p3R_5tr5tr_l0g1c_buG}`
