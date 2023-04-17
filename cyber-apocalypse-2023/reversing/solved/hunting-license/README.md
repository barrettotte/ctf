# hunting-license

**SOLVED**

> STOP! Adventurer, have you got an up to date relic hunting license? 
> If you don't, you'll need to take the exam again before you'll be allowed passage into the spacelanes!

```sh
strings license
# PasswordNumeroUno
# 0wTdr0wss4P => P4ssw0rdTw0
# G{zawR}wUz}r  => cyberchef XOR(13)
```

Ghidra

main > exam, xor

```

                             t2                                              XREF[3]:     Entry Point(*), exam:00401361(*), 
                                                                                          exam:00401361(*)  
        00404070 47 7b 7a        undefine
                 61 77 52 
                 7d 77 55 
           00404070 47              undefined147h                     [0]                               XREF[3]:     Entry Point(*), exam:00401361(*), 
                                                                                                                     exam:00401361(*)  
           00404071 7b              undefined17Bh                     [1]
           00404072 7a              undefined17Ah                     [2]
           00404073 61              undefined161h                     [3]
           00404074 77              undefined177h                     [4]
           00404075 52              undefined152h                     [5]
           00404076 7d              undefined17Dh                     [6]
           00404077 77              undefined177h                     [7]
           00404078 55              undefined155h                     [8]
           00404079 7a              undefined17Ah                     [9]
           0040407a 7d              undefined17Dh                     [10]
           0040407b 72              undefined172h                     [11]
           0040407c 7f              undefined17Fh                     [12]
           0040407d 32              undefined132h                     [13]
           0040407e 32              undefined132h                     [14]
           0040407f 32              undefined132h                     [15]
           00404080 13              undefined113h                     [16]
```


477b7a6177527d77557a7d727f32323213

```c
  xor(&local_38,t2,0x11,0x13); // 17 bytes, xor with 0x13
  local_10 = (char *)readline("Your final test - give me the third, and most protected, password: ")
  ;
  iVar1 = strcmp(local_10,(char *)&local_38);
```

`solve.py`

ThirdAndFinal!!!

- `nc 159.65.81.51 30314`

- `file license` - ELF
- `readelf -a license` - x86
- `ldd license` - libreadline
- address of main? - `nm license | grep main` - 0x401172 NOPE
- ghidra - 5
- PasswordNumeroUno
- 0wTdr0wss4P
- P4ssw0rdTw0
- 0x13
- ThirdAndFinal!!!

`HTB{l1c3ns3_4cquir3d-hunt1ng_t1m3!}`
