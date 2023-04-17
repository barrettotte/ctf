# she-shells-c-shells

**SOLVED**

> You've arrived in the Galactic Archive, sure that a critical clue is hidden here. 
> You wait anxiously for a terminal to boot up, hiding in the shadows from the guards hunting for you. 
> Unfortunately, it looks like you'll need a password to get what you need without setting off the alarms...

```sh
strings shell
```

```c
  fgets((char *)&local_118,0x100,stdin);
  for (local_c = 0; local_c < 0x4d; local_c = local_c + 1) {
    *(byte *)((long)&local_118 + (long)(int)local_c) =
         *(byte *)((long)&local_118 + (long)(int)local_c) ^ m1[(int)local_c];
  }
  local_14 = memcmp(&local_118,t,0x4d);
  if (local_14 == 0) {
    for (local_10 = 0; local_10 < 0x4d; local_10 = local_10 + 1) {
      *(byte *)((long)&local_118 + (long)(int)local_10) =
           *(byte *)((long)&local_118 + (long)(int)local_10) ^ m2[(int)local_10];
    }
    printf("Flag: %s\n",&local_118);
    uVar1 = 0;
  }
  else {
    uVar1 = 0xffffffff;
  }
  return uVar1;
```

t is label in memory
0x4d = 77

input of stdin into local_118 needs to be 77 bytes and equal to t

```txt
                             t                                               XREF[1]:     func_flag:0010193b(*)  
        00102200 2c 4a b7        undefine
                 99 a3 e5 
                 70 78 93 
           00102200 2c              undefined12Ch                     [0]                               XREF[1]:     func_flag:0010193b(*)  
           00102201 4a              undefined14Ah                     [1]
           00102202 b7              undefined1B7h                     [2]
           00102203 99              undefined199h                     [3]
           00102204 a3              undefined1A3h                     [4]
           00102205 e5              undefined1E5h                     [5]
           00102206 70              undefined170h                     [6]
           00102207 78              undefined178h                     [7]
           00102208 93              undefined193h                     [8]
           00102209 6e              undefined16Eh                     [9]
           0010220a 97              undefined197h                     [10]
           0010220b d9              undefined1D9h                     [11]
           0010220c 47              undefined147h                     [12]
           0010220d 6d              undefined16Dh                     [13]
           0010220e 38              undefined138h                     [14]
           0010220f bd              undefined1BDh                     [15]
           00102210 ff              undefined1FFh                     [16]
           00102211 bb              undefined1BBh                     [17]
           00102212 85              undefined185h                     [18]
           00102213 99              undefined199h                     [19]
           00102214 6f              undefined16Fh                     [20]
           00102215 e1              undefined1E1h                     [21]
           00102216 4a              undefined14Ah                     [22]
           00102217 ab              undefined1ABh                     [23]
           00102218 74              undefined174h                     [24]
           00102219 c3              undefined1C3h                     [25]
           0010221a 7b              undefined17Bh                     [26]
           0010221b a8              undefined1A8h                     [27]
           0010221c b2              undefined1B2h                     [28]
           0010221d 9f              undefined19Fh                     [29]
           0010221e d7              undefined1D7h                     [30]
           0010221f ec              undefined1ECh                     [31]
           00102220 eb              undefined1EBh                     [32]
           00102221 cd              undefined1CDh                     [33]
           00102222 63              undefined163h                     [34]
           00102223 b2              undefined1B2h                     [35]
           00102224 39              undefined139h                     [36]
           00102225 23              undefined123h                     [37]
           00102226 e1              undefined1E1h                     [38]
           00102227 84              undefined184h                     [39]
           00102228 92              undefined192h                     [40]
           00102229 96              undefined196h                     [41]
           0010222a 09              undefined109h                     [42]
           0010222b c6              undefined1C6h                     [43]
           0010222c 99              undefined199h                     [44]
           0010222d f2              undefined1F2h                     [45]
           0010222e 58              undefined158h                     [46]
           0010222f fa              undefined1FAh                     [47]
           00102230 cb              undefined1CBh                     [48]
           00102231 6f              undefined16Fh                     [49]
           00102232 6f              undefined16Fh                     [50]
           00102233 5e              undefined15Eh                     [51]
           00102234 1f              undefined11Fh                     [52]
           00102235 be              undefined1BEh                     [53]
           00102236 2b              undefined12Bh                     [54]
           00102237 13              undefined113h                     [55]
           00102238 8e              undefined18Eh                     [56]
           00102239 a5              undefined1A5h                     [57]
           0010223a a9              undefined1A9h                     [58]
           0010223b 99              undefined199h                     [59]
           0010223c 93              undefined193h                     [60]
           0010223d ab              undefined1ABh                     [61]
           0010223e 8f              undefined18Fh                     [62]
           0010223f 70              undefined170h                     [63]
           00102240 1c              undefined11Ch                     [64]
           00102241 c0              undefined1C0h                     [65]
           00102242 c4              undefined1C4h                     [66]
           00102243 3e              undefined13Eh                     [67]
           00102244 a6              undefined1A6h                     [68]
           00102245 fe              undefined1FEh                     [69]
           00102246 93              undefined193h                     [70]
           00102247 35              undefined135h                     [71]
           00102248 90              undefined190h                     [72]
           00102249 c3              undefined1C3h                     [73]
           0010224a c9              undefined1C9h                     [74]
           0010224b 10              undefined110h                     [75]
           0010224c e9              undefined1E9h                     [76]
```

t  -> 2c4ab799a3e57078936e97d9476d38bdffbb85996fe14aab74c37ba8b29fd7ecebcd63b23923e184929609c699f258facb6f6f5e1fbe2b138ea5a99993ab8f701cc0c43ea6fe933590c3c910e9

m1 -> 6e3fc3b9d78d1558e50ffbac224d57dbdfcfedfc1c846ad81ca617c4c1bfa08587a143d4584f8da8b2f27ca3b98637dabf070a7e73df5c60aecacfb9e0deff0070b9e45fc89ab351f5aea87e8d

`HTB{cr4ck1ng_0p3n_sh3ll5_by_th3_s34_sh0r3}`
