# janken

**SOLVED**

> As you approach an ancient tomb, you're met with a wise guru who guards its entrance. 
> In order to proceed, he challenges you to a game of Janken, a variation of rock paper scissors with a unique twist. 
> But there's a catch: you must win 100 rounds in a row to pass. 
> Fail to do so, and you'll be denied entry.

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
