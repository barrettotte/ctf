# RTL Easy

They said they added a layer of encryption, do you think you can still get in?

## Solution

```py
def enc(din):
    temp = (din & 0x3FF)
    temp = temp << 2
    temp = temp ^ 0xA
    dout = (temp >> 2)
    dout = dout & 0xFF
    return dout

ciph = b"RAVDyJBpf]Glap{rvkml]kq]1cq{"

for x in ciph:
    for i in range(255):
        if enc(i) == x:
            print(chr(i), end="")
```
use hex values in provided image...

## Attempt

svg is a waveform with `dout`:

0h52 0h41 0h56 0h44 0h79 0h4a 0h42 0h70 
0h66 0h5d 0h47 0h6c 0h61 0h70 0h7b 0h72 
0h76 0h6b 0h6d 0h6c 0h5d 0h6b 0h71 0h5d 
0h31 0h63 0h71 0h7b

0x52415644794a4270665d476c61707b72766b6d6c5d6b715d3163717b
