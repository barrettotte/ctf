# unbreakable

Think you can escape my grasp? Challenge accepted! 
I dare you to try and break free, but beware, it won't be easy. 
I'm ready for whatever tricks you have up your sleeve!

## Solution

```txt
input
globals

open('flag.txt','r').read

exec(input())

exec(input())
print(open("flag.txt", "r").read())
```

`nc 94.237.50.221 53625`

HTB{3v4l_0r_3vuln??}

## Post-CTF

https://youtu.be/EGItzKCxTdQ?si=SblP19F4q7klkAPx&t=8572

Apparently python accepts unicode 'b' (U+FF42)

pass breakpoint with a unicode 'b'

```
# opens python debugger

import os
os.system('cat flag.txt')
```
