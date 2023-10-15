# lock-the-lock

Unlock the Unlocked

## Solution

```txt
Validation based on certain numbers location on an avltree. 
right means 1 and left means 0. 
Decompile the pyc into py. 
be careful, the decompiled code might result different than the original pyc. 

So if the decompiled says correct but the value seems odd, 
try submitting it on the original pyc, 
analyze the problem, 
and fix the decompiled code.
```

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Reverse%20Engineering/Lock%20the%20Lock/writeup/solve.py

From discord:

https://github.com/SuperStormer/writeups/blob/master/tcp1pctf_2023/rev/lock_the_lock/lock.py

- decompile the pyc w/ decompyle3
- fix lendis.insert decompilation by looking at the pycdc output 
- then you see that lendis.check basically wants you to find the path to a node with a specific value in a binary tree
- so just use DFS (or BFS, doesn't matter) to map values to paths
