# debug-me

debug me and get the flag!

## Solution

gdpscript from discord

```py
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

gdb.execute("file ./main")
gdb.execute("set disassembly-flavor intel")
gdb.execute("r < /dev/null")

x=open('./input','w+')
x.write("a"*0x48+"\n")
x.close()

gdb.execute("break *(0x555555554000+0x11C9)")#init0
gdb.execute("break *(0x555555554000+0x11ff)")#init1
gdb.execute("break *(0x555555554000+0x4cd66)")#cmp
gdb.execute("r < input")
gdb.execute("set $rip=0x555555554000+0x11Fe")#init0 ret
gdb.execute("c")
gdb.execute("set $rip=0x555555554000+0x12E2")#init1 ret
gdb.execute("c")
for i in range(0x48):
    rax=gdb.parse_and_eval("$rdx")
    eprint(chr(rax),end="")
    gdb.execute("set $rdx=$rax")
    gdb.execute("c")
gdb.execute("exit")
```
