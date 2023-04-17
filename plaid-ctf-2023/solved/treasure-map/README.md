# treasure-map

http://treasure.chal.pwni.ng/

checked js, `0.js`

debugger -> `0-200.js`

```js
window.check = async () => {
    clear();
    let flag = document.querySelector("#input").value;
    if (!flag.startsWith("PCTF{") || !flag.endsWith("}")) {
        await fail();
        return;
    }

    flag = flag.slice(5, -1);
    if (flag.length != 25) {
        await fail();
        return;
    }

    window.buffer = flag.split("");
    go();
}
```

`PCTF{AAAAAAAAAAAAAAAAAAAAAAAAA}`

did something?... eventually fails

16
60
136
75
189
53
37
115
171 <- stuck here loops on 171


https://en.wikipedia.org/wiki/Variable-length_quantity

https://www.murzwin.com/base64vlq.html

```
0.js.map
"mappings": ";A4DAA;A0DAA;AzEAA;AsDAA;AmGAA;AtIAA;ApBAA;A8DAA;AZAA;AxDAA;AyDAA;ALAA;A9EAA;A6HAA;AoBAA;A1BAA;A7BAA;AvCAA;AwEAA;AFAA;AuBAA;A8BAA;AHAA;AnGAA;AvBAA;A+GAA;A2BAA;A/EAA;A7CAA;ALAA;ArCAA;AqJAA;AxCAA;AoDAA;AGAA;AtEAA;AtDAA;AjEAA;AYAA;AiFAA;AhBAA;ArEAA;AkJAA;AlCAA;A9GAA;AkHAA;AnFAA;AMAA;A5CAA;AgCAA;AyJAA;AhDAA;AjFAA;AoDAA;A/FAA;A+HAA;AzIAA;A6CAA;AsBAA;A4FAA;AvFAA;A4BAA;A1DAA;A4CAA;AoGAA"

([0,0](#60)=>[1,0])     A
([0,0](#118)=>[2,0])    B
([0,0](#45)=>[3,0])     C
([0,0](#99)=>[4,0])     D
([0,0](#198)=>[5,0])    E
([0,0](#64)=>[6,0])     F
([0,0](#44)=>[7,0])     G
([0,0](#106)=>[8,0])    H
([0,0](#94)=>[9,0])     I
([0,0](#38)=>[10,0])    J
([0,0](#95)=>[11,0])    K
([0,0](#90)=>[12,0])    L
([0,0](#12)=>[13,0])    M
([0,0](#137)=>[14,0])   N
([0,0](#157)=>[15,0])   O
([0,0](#131)=>[16,0])   P
([0,0](#102)=>[17,0])   Q
([0,0](#63)=>[18,0])    R
([0,0](#135)=>[19,0])   S 
([0,0](#133)=>[20,0])   T
([0,0](#156)=>[21,0])   U
([0,0](#186)=>[22,0])   V
([0,0](#183)=>[23,0])   W
([0,0](#84)=>[24,0])    X
([0,0](#61)=>[25,0])    Y
([0,0](#172)=>[26,0])   Z
([0,0](#199)=>[27,0])   a
([0,0](#120)=>[28,0])   b
([0,0](#75)=>[29,0])    c
([0,0](#70)=>[30,0])    d
([0,0](#33)=>[31,0])    e
([0,0](#182)=>[32,0])   f
([0,0](#142)=>[33,0])   g
([0,0](#194)=>[34,0])   h
([0,0](#197)=>[35,0])   i
([0,0](#127)=>[36,0])   j
([0,0](#73)=>[37,0])    k
([0,0](#8)=>[38,0])     l
([0,0](#20)=>[39,0])    m
([0,0](#101)=>[40,0])   n
([0,0](#85)=>[41,0])    o
([0,0](#16)=>[42,0])    p
([0,0](#162)=>[43,0])   q
([0,0](#128)=>[44,0])   r
([0,0](#18)=>[45,0])    s
([0,0](#132)=>[46,0])   t
([0,0](#49)=>[47,0])    u
([0,0](#55)=>[48,0])    v
([0,0](#11)=>[49,0])    w
([0,0](#43)=>[50,0])    x
([0,0](#196)=>[51,0])   y
([0,0](#148)=>[52,0])   z
([0,0](#67)=>[53,0])    0
([0,0](#119)=>[54,0])   1
([0,0](#24)=>[55,0])    2
([0,0](#151)=>[56,0])   3
([0,0](#14)=>[57,0])    4
([0,0](#59)=>[58,0])    5
([0,0](#81)=>[59,0])    6
([0,0](#173)=>[60,0])   7
([0,0](#86)=>[61,0])    8
([0,0](#114)=>[62,0])   9
([0,0](#56)=>[63,0])    +
([0,0](#100)=>[64,0])   /
([0,0](#200)=>[65,0])   =
```

seems like output of all that js garbage is just reading the mapping file to determine the next js file to go to...

200 == fail
201 == success

find path to get to 201->success

1  - A
2  - B
3  - C
4  - D
5  - E
6  - F
7  - G
8  - H
9  - I
10 - J
11 - K
12 - L
13 - M
14 - N
15 - O
16 - P
17 - Q
18 - R
19 - S
20 - T
21 - U
22 - V
23 - W
24 - X
25 - Y
26 - Z
27 - a
28 - b
29 - c
30 - d
31 - e
32 - f
33 - g
34 - h
35 - i
36 - j
37 - k
38 - l
39 - m
40 - n
41 - o
42 - p
43 - q
44 - r
45 - s
46 - t
47 - u
48 - v
49 - w
50 - x
51 - y
52 - z
53 - 0
54 - 1
55 - 2
56 - 3
57 - 4
58 - 5
59 - 6
60 - 7
61 - 8
62 - 9
63 - +
64 - /
=

ran `base64vlq.py`, #201 is 41.js
start from 41 and work back?

201
41     
21     0
32     0
72     2
126    +
147    t
42     u
167    o
34     b
123    a
169    +
92     w
26     o
110    H
74     /
181    p
83     a
19     m
50     +
192    a
160    +
137    d
28     e
137    e
0      N

Need+a+map/How+about+200

PCTF{Need+a+map/How+about+200}

missing a char...needs to be 25
bruteforcing...nope waste of time

```
41.js.map

71) [[83, 1, 0, 0], [1, -1, 0, 0]]        [0,201](#201)=>[71,83]
71) [[83, 1, 0, 0], [1, -1, 0, 0]]        [0,200](#200)=>[71,84]
```

oh wtf its '!', one line down...

`PCTF{Need+a+map/How+about+200!}`
