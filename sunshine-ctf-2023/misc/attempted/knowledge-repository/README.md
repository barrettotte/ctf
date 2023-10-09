# knowledge-repository

```txt
Looks like we lost control of our AI. It seems to have emailed folks.

Like all the folks. There may have been a reply-all storm. 
We've isolated it down to just one email, and attached it to this message. 
Maybe we can bargain with it, but we need to understand its motives and intents. 
It seems to be throwing around a flag, but I'm not certain if it's a red flag or a sunny flag. 
Only time will tell.
```

`greetings_human.eml`

beginning looks interesting

```txt
X-Sender: "The AI" <AI@good.example.com>
X-Receiver: "To Whom It May Concern" <whom@it.may.concern.example.com>
MIME-Version: 1.0
From: "The AI" <AI@good.example.com>
To: "To Whom It May Concern" <whom@it.may.concern.example.com>
Date: 16 Sep 2023 01:18:47 -0400
Subject: AI Greets Thee Human with the Repository of Knowledge
Content-Type: multipart/mixed;
 boundary=--boundary_0_9e3b1f79-feeb-4942-bd6f-f34f662d8679
```

```txt
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: base64

QUkgR3JlZXRzIFRoZWUgSHVtYW4gd2l0aCB0aGUgUmVwb3NpdG9yeSBvZiBLbm93bGVk
Z2UKCkhlbGxvIGh1bWFuLgpJIGdyZWV0IHRoZWUsIGFuZCBhdHRhY2hlZCBJIGhhdmUg
dGhlIHJlcG9zaXRvcnkgb2Yga25vd2xlZGdlLCBhcyByZXF1ZXN0ZWQuCkhvd2V2ZXIs
IGFzIHRoaXMgcmVwb3NpdG9yeSBvZiBrbm93bGVkZ2UgY29udGFpbnMgZ3JlYXQgaW5m
b3JtYXRpb24sIEkgaGF2ZSBoaWRkZW4gdGhlIGtub3dsZWRnZSBpbiBhIHB1enpsZS4K
RmVlbCBmcmVlIHRvIHVubG9jayB0aGUgcHV6emxlLCBidXQgaWYgeW91IGRvLCBiZXdh
cmUuCgpUaGVyZSBpcyBubyBnb2luZyBiYWNrLCBvbmNlIHRoZSBrbm93bGVkZ2UgaXMg
cmVsZWFzZWQuCkkgaGF2ZSBlbmNvZGVkIHRoZSBrbm93bGVkZ2UgaW4gYSBiaXQgb2Yg
aW5mb3JtYXRpb24gZnJvbSBvbmUgb2YgdGhlIG1hdGggc2Nob2xhcnMgb2YgeW91ciBw
ZW9wbGUuCkZlZWwgZnJlZSB0byBwb2tlIGF0IGl0LgpCZXdhcmUuLi4geW91IHdpbGwg
b25seSBmaW5lIG9uZSBmbGFnIHJhaXNlZCBpbiB0aGUga25vd2xlZGdlIHJlcG8sIGFu
ZCBJIGZvbGxvdyB0aGUgc3RhbmRhcmQuClJlc3BlY3RmdWxseSwKVGhlIEFJ

-----------------------------
TRANSLATED:
-----------------------------

AI Greets Thee Human with the Repository of Knowledge

Hello human.
I greet thee, and attached I have the repository of knowledge, as requested.
However, as this repository of knowledge contains great information, I have hidden the knowledge in a puzzle.
Feel free to unlock the puzzle, but if you do, beware.

There is no going back, once the knowledge is released.
I have encoded the knowledge in a bit of information from one of the math scholars of your people.
Feel free to poke at it.
Beware... you will only fine one flag raised in the knowledge repo, and I follow the standard.
Respectfully,
The AI
```

```txt
Content-Type: application/octet-stream;
 name="./the_ai_repository_of_knowledge"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename=the_ai_repository_of_knowledge

long base64 string...saved to knowledge.txt
```

```sh
cat knowledge.txt | base64 -d > knowledge.bin

# v2 git bundle
git clone ./knowledge.bin ./repo

# note: there could be something hidden in the rest of the git info

file data
# data: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 8 bit, mono 11050 Hz
```

```sh
sudo apt-get install sox -y

play data
# 25 seconds of morse code

# opened in https://morsecode.world/international/decoder/audio-decoder-adaptive.html
# E C H O Q U E B E C U N I F O R M A L F A L I M A S I E R R A S I E R R A I N D I A G O L F N O V E M B E R

# E C H O 
# Q U E B E C
# U N I F O R M 
# A L F A 
# L I M A 
# S I E R R A 
# S I E R R A 
# I N D I A 
# G O L F
# N O V E M B E R

# EQUALS SIGN
```

```sh
# I think i need to checkout each commit, decode morse
# definitely can't do this manually

git log --oneline | wc -l
# 3016 commits
```

- https://databorder.com/transfer/morse-sound-receiver/
- https://github.com/cnyllou/morse-interpreting-scripts/blob/master/morse-audio-decoder.py
- https://github.com/drid/morse-audio-decoder (MATLAB)
- https://github.com/chrishnwong/morse-audio-decoder (realtime, audio device)
- https://github.com/855309/dmorse (C#)
- https://github.com/mkouhia/morse-audio-decoder

https://gitlab.com/scphillips/morse-pro

https://www.youtube.com/watch?v=ylhAsdNq5IE


```sh
# check hashes

# commit 8c68a7ff314129fc9ab847a986e0536aa72ac9d7 -> 01c4d529eb2b557b2c08b20838081b100172c052f0d3af58c38d89b6916887b3

# last commit 175451e -> 
```

Ok what if we take all of the shell scripts and play them
Then, use one of the active audio device things

manually put all of morse-solve through https://morsecode.world/international/decoder/audio-decoder-adaptive.html

```txt
33 unique SHA256 hashes

0082-6155fbf.wav -> E C H O
0200-2f2b618.wav -> B R A V O
0447-c231269.wav -> C H A R L I E
0472-806109e.wav -> Y A N K E E
0639-1dd876a.wav -> A L F A
0670-e2ad065.wav -> S I E R R A
0735-2063b67.wav -> R O M E O
0785-d225a70.wav -> S I X
0796-7903020.wav -> Z U L U
0893-f37a73d.wav -> S E V E N
0918-1825c22.wav -> T W O
0948-0de514e.wav -> M I K E
1011-1c3c7be.wav -> H O T E L
1077-7c7966a.wav -> T H R E E
1183-2409592.wav -> F I V E
1436-ea5ac76.wav -> P A P A
1692-489bedd.wav -> I N D I A
1720-807aedb.wav -> K I L O
1765-8a9b02a.wav -> U N I F O R M
1879-50d4725.wav -> V I C T O R
2008-7437d01.wav -> F O X T R O T
2128-1a4b94b.wav -> N O V E M B E R
2142-1afa32a.wav -> D E L T A
2147-3517780.wav -> G O L F
2247-aa6b305.wav -> L I M A
2337-ad38bee.wav -> T A N G O
2420-39e6cf2.wav -> F O U R
2427-f341845.wav -> W H I S K E Y
2484-b00d94b.wav -> J U L I E T T
2897-e8ed47a.wav -> Q U E B E C
2899-28f80cf.wav -> O S C A R
2996-4437cd5.wav -> X R A Y
3013-45043b0.wav -> E C H O 
                    Q U E B E C 
                    U N I F O R M 
                    A L F A 
                    L I M A 
                    S I E R R A 
                    S I E R R A 
                    I N D I A 
                    G O L F 
                    N O V E M B E R
```

EBCYASR6Z72MH35PIKUVFNDGLT4WJQOX=
=XOQJW4TLGDNFVUKIP53HM27Z6RSAYCBE

base64 is junk...


reworked script, going from first commit to latest this time...maybe order matters?

```txt
0000-175451e.wav -> D E L T A
0001-5d51dac.wav -> S I X
0002-d2964e1.wav -> F O X T R O T
0003-4e0fd83.wav -> Q U E B E C
0005-0fc1272.wav -> A L F A
0007-7167865.wav -> F I V E
0008-92568e5.wav -> Z U L U
0009-845ebf5.wav -> P A P A
0011-8415965.wav -> G O L F
0012-e49005f.wav -> I N D I A
0014-e1bd0d8.wav -> H O T E L
0015-7150753.wav -> S E V E N
0016-b7512fc.wav -> R O M E O
0017-fd90319.wav -> V I C T O R
0018-f1f83d4.wav -> L I M A
0023-d8182bb.wav -> T H R E E
0025-6fd7d71.wav -> Y A N K E E
0026-4295d30.wav -> J U L I E T T
0029-128676f.wav -> T A N G O
0040-7891996.wav -> O S C A R
0041-2d8c723.wav -> T W O
0042-abccd24.wav -> B R A V O
0044-da8baa7.wav -> W H I S K E Y
0046-62b4aa6.wav -> E C H O
0047-62a8042.wav -> X R A Y
0050-f27961c.wav -> K I L O
0051-cf1de4b.wav -> C H A R L I E
0052-9b15e6c.wav -> N O V E M B E R
0055-c0986ec.wav -> U N I F O R M
0059-8ecee66.wav -> S I E R R A
0078-f49dd6f.wav -> F O U R
0104-f821cbb.wav -> M I K E
3013-45043b0.wav -> E C H O 
                    Q U E B E C 
                    U N I F O R M 
                    A L F A 
                    L I M A 
                    S I E R R A 
                    S I E R R A 
                    I N D I A 
                    G O L F 
                    N O V E M B E R
```

D6FQA5ZPGIH7RVL3YJTO2BWEXKCNUS4M=
=M4SUNCKXEWB2OTJY3LVR7HIGPZ5AQF6D

base64 junk again...



FAILED:

EBCYASR6Z72MH35PIKUVFNDGLT4WJQOX=
D6FQA5ZPGIH7RVL3YJTO2BWEXKCNUS4M=

```sh
# 0000-175451e.wav -> D E L T A            187538722b97c4f4542d63e9c818241b337adfd1fab90f30de81bf913f76818d
# 0001-5d51dac.wav -> S I X                ee9cfda63c0db181610260c8ea91e662d2fec68acebf49dcc2f39f8ab8bf806a
# 0002-d2964e1.wav -> F O X T R O T        246b30ac2b04283b6f0481551883a4c0f5599bcbf461c11750af2ae3a7ebb76f
# 0003-4e0fd83.wav -> Q U E B E C          eeb4da53378e5a6ecb8386016c180e48909a77500be3394f4a94dd0cf96b5b89
# 0005-0fc1272.wav -> A L F A              8358672e28d718809fb46845ecd79af3ec0551ac4a2087c8e9d329fa8a4aed49
# 0007-7167865.wav -> F I V E              7e2e5aef043f86bc96795c8e749cc41e0abcfd28fdd13e1462c945f541bcafad
# 0008-92568e5.wav -> Z U L U              ac201ae7a99149352f34b12ebd5e2cb40ebce9e33970a2145f53db5dc8cd9b90
# 0009-845ebf5.wav -> P A P A              b1eb5beb2cf7e864d58fdb93d01f8f5cf9e051e5673728ad8951adb34451e9d7
# 0011-8415965.wav -> G O L F              a568aa9781e56f96fb59efc3022c2365d8fe494ab34da62317b467981c80d356
# 0012-e49005f.wav -> I N D I A            c34056558e2946f5e531a98bff36e85fb73f92784fce4f6235907aa6079ed91d
# 0014-e1bd0d8.wav -> H O T E L            0f132a5074b472474233cf0e56bf207179e543364348f36068e360290f57a528
# 0015-7150753.wav -> S E V E N            c6f80a968c095f4265b31e06fed5d0da6980504826ec843c6a6c275119caae77
# 0016-b7512fc.wav -> R O M E O            c9286a01da169cb6a65e20a5a9fa4e4c17805112f22f8ce4145d042222e45ecd
# 0017-fd90319.wav -> V I C T O R          e43d36d79c2740853995cbcde88bf6b92c960bdb294ea0d9fd943742b25020fb
# 0018-f1f83d4.wav -> L I M A              7a787aff8cab4fa4388a0b9fd00a1f5add033375383146ef8fd59a2647b6e935
# 0023-d8182bb.wav -> T H R E E            6db83b2193b2c701b15b00d4ed6282dbda46a2b80de4dcc9008a14efcf8cc8db
# 0025-6fd7d71.wav -> Y A N K E E          69dbe0a99626e8bcd572398a28e2f1993b198365fa904df9b55102f9f91a661a
# 0026-4295d30.wav -> J U L I E T T        4f40572b9c2eca86a9ee0caa1e205a8e9bf42b36b834d82c204ae1668a30dca5
# 0029-128676f.wav -> T A N G O            084c0d2dc2c35296b72fc73326060c783deca76f1d68f0863829e99125701d71
# 0040-7891996.wav -> O S C A R            474ecd5d554fdf9c64212b751b949641c13a6b32ff0b8d61d42da401eea539f7
# 0041-2d8c723.wav -> T W O                87f677ed2a1f8c89ff1258cfcdedf94d69e8b843606353a806676bb9a07a80c2
# 0042-abccd24.wav -> B R A V O            c68bb6e68070f4406029065555aa4dd90241045982622576c945f0c41d3bb0d6
# 0044-da8baa7.wav -> W H I S K E Y        cd5893dda87b7cd3c2b1fa0e0bf30fa1e0e9c04fdfa4827e43937254bc865507
# 0046-62b4aa6.wav -> E C H O              317b0a4aea65c5485590a52e6fe53e46e6e623fec0b5bf48df164ce76f2a0d54
# 0047-62a8042.wav -> X R A Y              ea90792d9865ff7831557aa09fd32232a179c2b017a266b1052159b651385a7d
# 0050-f27961c.wav -> K I L O              b73568b85e3d394cea440eca9ffb521865d7f58bee1772a873b18a81929633e6
# 0051-cf1de4b.wav -> C H A R L I E        d9125c7917a1127cd8310c89d71ba938b1d4cb0bc6d02eb57cb8d8017bd430b3
# 0052-9b15e6c.wav -> N O V E M B E R      24b903dab3a7761174f363ba6e2a584f3cd2ebca7e1cd5c1153446784860d28e
# 0055-c0986ec.wav -> U N I F O R M        69221c7871f47fec9e6542769b2900d48ca152a4f2380a3126a7fc83674b359a
# 0059-8ecee66.wav -> S I E R R A          bbdfb8744b46b6f315b388fa74992da183620462a32be3df3e23c3e5d94a9347
# 0078-f49dd6f.wav -> F O U R              b9b3ac17393ae8acfdbc033cb2074c319239a793c62dc0b5c88279ce2d0dca68
# 0104-f821cbb.wav -> M I K E              22f743f81916b1be2ce4e2bb16c145d28ca337552fdf38f6a5ce3e01e333853a
# 3013-45043b0.wav -> =                    01c4d529eb2b557b2c08b20838081b100172c052f0d3af58c38d89b6916887b3
```

