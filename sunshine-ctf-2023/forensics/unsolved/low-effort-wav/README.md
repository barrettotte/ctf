# low-effort-wav

https://github.com/D13David/ctf-writeups/blob/main/sunshinectf23/forensics/low_effort_wave/README.md

```sh
$ file low_effort.wav
low_effort.wav: PNG image data, 465 x 803, 8-bit/color RGBA, non-interlaced.
```

wav file is an image, but the image itself is cropped

Apparently there's something called https://en.wikipedia.org/wiki/ACropalypse

A vulnerability in screenshot tools for Google Pixel phones...The EXIF data I found during my attempt
using exiftool shows the GooglePixel 7 as the source phone...should have thought to look this up!

https://acropalypse.app/

This recovers the flag

Also https://youtu.be/qA6ajf7qZtQ?si=mwM3oO20qzyxBXkl&t=371

There's two IEND chunks when there should only be 1
