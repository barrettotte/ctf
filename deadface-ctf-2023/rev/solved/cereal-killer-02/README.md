# cereal-killer-02

`luciafer` can be a bit of trouble sometimes, but she can put away the sugary monster cereals with the best of them! 
She has a favorite, too, and it is based on her favorite monster. 
See if you can figure it out! Select the binary for your preferred platform.

## Solution

```sh
strings re02.bin

```

ghidra

maybe try angr?

```sh
pip3 install angr

readelf -a re02.bin
```

0x56556246


// CORRECT!!!!!
// DAT_00012094[13] = 08 3D 33 3F 15 36 32 47 52 12 1B 65
// payload = 

// 4B 72 31 7E 40 72 63 13 02 46 75

43 0a 4f 0a 52 0a 45 0a 43 0a 54 0a 21

C 43 
O 4f
R 52
E 45
C 43
T 54
! 21

A XOR B = R -> B = A XOR R

A = 08 3D 33 3F 15 36 32 47 52 12 1B 65   083D333F1536324752121B65
R = 43 4F 52 52 45 43 54 21 21 21 21 21   434F52524543542121212121
B = ?

`xor.py` 0x4b72616d5075666673333a44

`KramPuffs3:D`

`flag{GramPa-KRAMpus-Is-Comin-For-Da-Bad-Kids!!!}`
