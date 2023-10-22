# the-wisdom-of-knox

Oh, Why Should the Spirit of Mortal be Proud?

by William Knox, 1789 – 1825

I. Oh, why should the spirit of mortal be proud?
Like a swift-fleeing meteor, a fast-flying cloud,
A flash of the Lightning, a break of the wave,
Man passes from life to his rest in the grave.

II. The leaves of the oak and the willow shall fade,
Be scattered around and together be laid;
And the young and the old, and the low and the high,
Shall molder to dust and together shall lie.

III. The infant, a mother attended and, loved,
The mother, that infant’s affection who proved,
The husband, that mother and infant who blessed,
Each, all, are away to their dwellings of rest.

IV. The maid, on whose cheek, on whose brow, in whose eye,
Shone beauty and pleasure––her triumphs are by;
And the memories of those who have loved her and praised
Are alike from the minds of the living erased.

## Solution

Same deal, end up with `heP3fXSv8WpeAaBwXNnKv1xjUDfdauBjhVhMwjxnFPfQ2Zin4gKXN7o5pKjxYdotNz5ern57Dk2xX`
from bottom of page

Cyberchef, magic ... for some reason mine didn't work? Maybe I was doing something dumb

base58 -> EBCDIC

`flag{WHY?-Because-We-Are-31337-H4X0RZ-H4CK-DA-PLANET!!!}`

Also, apparently the cipher above can literally just be found by `cat wok.txt`

## My Attempt

```
Infra vexillum secretum est
ըեՐԳզ՘ՓնԸ՗հեՁաՂշ՘ՎծՋնԱոժՕՄզդայՂժըՖըՍշժոծՆՐզՑԲ՚թծԴէՋ՘ՎԷկԵհՋժոՙդկմՎպԵեղծԵԷՄիԲո՘

latin: Below is the secret flag
```

```
aAVlBVAFMwVmBVgFUwV2BTgFVwVwBWUFQQVhBUIFdwVYBU4FbgVLBXYFMQV4BWoFVQVEBWYFZAVhBXUFQgVqBWgFVgVoBU0FdwVqBXgFbgVGBVAFZgVRBTIFWgVpBW4FNAVnBUsFWAVOBTcFbwU1BXAFSwVqBXgFWQVkBW8FdAVOBXoFNQVlBXIFbgU1BTcFRAVrBTIFeAVYBQo=
```

14 verses?


hint: Results are best when using Linux as opposed to jumping straight to CyberChef.

aAVlBVAFMwVmBVgFUwV2BTgFVwVwBWUFQQVhBUIFdwVYBU4FbgVLBXYFMQV4BWoFVQVEBWYFZAVhBXUFQgVqBWgFVgVoBU0FdwVqBXgFbgVGBVAFZgVRBTIFWgVpBW4FNAVnBUsFWAVOBTcFbwU1BXAFSwVqBXgFWQVkBW8FdAVOBXoFNQVlBXIFbgU1BTcFRAVrBTIFeAVYBQ==

68 05 65 05 50 05 33 05 66 05 58 05 53 05 76 05 38 05 57 05 70 05 65 05 41 05 61 05 42 05 77 05 58 05 4e 05 6e 05 4b 05 76 05 31 05 78 05 6a 05 55 05 44 05 66 05 64 05 61 05 75 05 42 05 6a 05 68 05 56 05 68 05 4d 05 77 05 6a 05 78 05 6e 05 46 05 50 05 66 05 51 05 32 05 5a 05 69 05 6e 05 34 05 67 05 4b 05 58 05 4e 05 37 05 6f 05 35 05 70 05 4b 05 6a 05 78 05 59 05 64 05 6f 05 74 05 4e 05 7a 05 35 05 65 05 72 05 6e 05 35 05 37 05 44 05 6b 05 32 05 78 05 58 05

68 65 50 33 66 58 53 76 38 57 70 65 41 61 42 77 58 4e 6e 4b 76 31 78 6a 55 44 66 64 61 75 42 6a 68 56 68 4d 77 6a 78 6e 46 50 66 51 32 5a 69 6e 34 67 4b 58 4e 37 6f 35 70 4b 6a 78 59 64 6f 74 4e 7a 35 65 72 6e 35 37 44 6b 32 78 58

68655033665853763857706541614277584e6e4b7631786a554466646175426a6856684d776a786e46506651325a696e34674b584e376f35704b6a7859646f744e7a3565726e3537446b327858

heP3fXSv8WpeAaBwXNnKv1xjUDfdauBjhVhMwjxnFPfQ2Zin4gKXN7o5pKjxYdotNz5ern57Dk2xX

https://snehasrees31.medium.com/snow-man-traboda-forensics-ctf-write-up-a3ae8a2e7851

```sh
sudo apt-get install -y stegsnow

stegsnow -C -p "heP3fXSv8WpeAaBwXNnKv1xjUDfdauBjhVhMwjxnFPfQ2Zin4gKXN7o5pKjxYdotNz5ern57Dk2xX" wok.txt

stegsnow -C -p "ըեՐԳզ՘ՓնԸ՗հեՁաՂշ՘ՎծՋնԱոժՕՄզդայՂժըՖըՍշժոծՆՐզՑԲ՚թծԴէՋ՘ՎԷկԵհՋժոՙդկմՎպԵեղծԵԷՄիԲո՘" wok.txt

stegsnow -C -p 'aAVlBVAFMwVmBVgFUwV2BTgFVwVwBWUFQQVhBUIFdwVYBU4FbgVLBXYFMQV4BWoFVQVEBWYFZAVhBXUFQgVqBWgFVgVoBU0FdwVqBXgFbgVGBVAFZgVRBTIFWgVpBW4FNAVnBUsFWAVOBTcFbwU1BXAFSwVqBXgFWQVkBW8FdAVOBXoFNQVlBXIFbgU1BTcFRAVrBTIFeAVYBQo=' wok.txt

stegsnow -C -p 'knox' wok.txt
```

```sh
grep -Po '^.' wok.txt | tr -d '\n'
```

heP3fXSv8WpeAaBwXNnKv1xjUDfdauBjhVhMwjxnFPfQ2Zin4gKXN7o5pKjxYdotNz5ern57Dk2xX
77 chars

https://www.dcode.fr/base62-encoding
03 E8 C3 5E 91 A0 26 85 95 FE A2 04 58 67 C9 25 A9 30 CB 21 AD BE F6 42 06 54 B7 2F 90 62 18 44 54 66 FC 44 AE 11 28 55 DE 3B 82 5B A9 BD FF 01 A6 FB 7E 5B 5C B5 9A AE 22 B3
nope


14 verses - 14 chars ? 
heP3fXSv8WpeAa


