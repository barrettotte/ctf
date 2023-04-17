# calibrator

> You found the spacectaft's route coordinates and decrypted them and you are finally ready to look them up.
> You boot up the spacectaft's map software. 
> The system powers up but you get prompted with an error during boot.
> Going through the error you assume the problem is caused by a faulty driver for the map's calibrator.
> After a few system restarts without success, you realize the existing driver is broken beyond repair.
> Your only hope is writting the calibration driver yourself and injecting to the system right before it boots up.
> Snooping through the vessel's archives you stumble upon the calibrator's manual which describes its functionality and information on how to build the driver firmware. 
> Can you build the driver so the calibration process terminates successfully?

TODO: review writeup

HTB discord:

```py
# method: perpendicular bisector of a chord passes through the centre of a circle

from pwn import *

r = remote('142.93.35.133', 32262)
r.recvuntil(b">")


def check(x, y,i=0):
    sending = f'{x} {y}'
    r.sendline(bytes(sending, 'utf-8'))
    if i != 46:
        recving = r.recvuntil(b'>')
    else:
        print(r.recvall())
        exit()
    result = None
    if "UNDETECTED" in str(recving):
        result = 0
    elif "DETECTED" in str(recving):
        result = 1
    elif "REFERENCE" in str(recving):
        result = 2
    if i == 46:
        print(recving)
    return result

for i in range(47):
    nx0 = -1000000000
    nx1 = 0
    px0 = 1000000000
    px1 = 0
    x = 0
    nx = 0
    px = 0
    while 1:
        x = nx0+((nx1-nx0)//2)
        if x == nx0 or x == nx1:
            nx = x
            break
        res = check(x,0)
        if res == 1:
            nx1 = x
        elif res == 0:
            nx0 = x

    x = 0
    while 1:
        x = px1+((px0-px1)//2)
        if x == px1 or x == px0:
            px = x
            break
        res = check(x,0)
        if res == 1:
            px1 = x
        elif res == 0:
            px0 = x

    midx = nx + ((px-nx)//2)

    ny0 = -1000000000
    ny1 = 0
    py0 = 1000000000
    py1 = 0
    y = 0
    ny = 0
    py = 0
    while 1:
        y = ny0+((ny1-ny0)//2)
        if y == ny0 or y == ny1:
            ny = y
            break
        res = check(midx,y)
        if res == 1:
            ny1 = y
        elif res == 0:
            ny0 = y

    y = 0
    while 1:
        y = py1+((py0-py1)//2)
        if y == py1 or y == py0:
            py = y
            break
        res = check(midx,y)
        if res == 1:
            py1 = y
        elif res == 0:
            py0 = y

    midy = ny + ((py-ny)//2)

    if check(midx,midy,i=i) == 2:
        print(f"we got center of circle {i}")
```