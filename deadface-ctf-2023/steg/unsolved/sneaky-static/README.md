# sneaky-static

We’ve intercepted a video from DEADFACE. 
According to Ghost Town, there is more to this image than it lets on. 
Figure out what kind of hidden message is in the video.

Submit the flag as flag{flag_here}.

## Solution

```sh
exiftool video.mp4
```

`ftyp` atom, search fo `ftyp` in a hex editor

two `ftyp` atoms found `0x00000000` and `0x001A73F7` (1733623)

Second video in side of this video

```sh
dd if=video.mp4 of=video_new.mp4 bs=1 skip=1733623
```

`flag{b3hind_th3_curT4iN}`

## My Attempt

```sh
file video.mp4
# video.mp4: ISO Media, MP4 v2 [ISO 14496-14]

```

```sh
# https://github.com/JavDomGom/videostego
make build

./videostego -r -f video.mp4
# no luck
```

