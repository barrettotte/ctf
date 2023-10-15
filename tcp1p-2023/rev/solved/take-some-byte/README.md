# take-some-byte

I think some code is need some effort to read

## Solution

python bytecode...I dont think we can decompile it

https://python.readthedocs.io/en/latest/library/dis.html#python-bytecode-instructions

worked through bytecode in `byte-solved.txt`

```txt
0   T
1   C
2   P
3   1
4   P
5   {
6   b
7   y
8   t
9   e
10     _?
11  c
12  o
13  d
14  e
15     _?
16  i
17  s
18     _?
19  H
20  u
21  F
22  t
23  t
24  
25  
```

TCP1P{byte_code_is_HuFtt}  ???? This isn't a word, but it worked ????

## Alternative Solutions

I could have used z3: https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Reverse%20Engineering/Take%20some%20Byte/writeup/solver.py

Also this exists: https://github.com/SuperStormer/pyasm
basically just converts the dis.dis output into a form that uncompyle6 can use
