# youve-been-ransomwared

DEADFACE is taunting GlitterCo with their latest ransomware attack. 
According to our intel, the attackers like to leave a calling card in their attacks. 
If we can figure out which DEADFACE actor executed this attack, we might be able to figure out a way around paying. 
Can you find anything in this screenshot that might point to which attacker ran this ransomware attack?

Submit the flag as flag{attacker_name}.

https://cyberhacktics.sfo2.digitaloceanspaces.com/DEADFACECTF2023/Challenges/steg/steg02/ransomwared.png

## Solution

- https://stegonline.georgeom.net/upload
- https://github.com/zed-0xff/zsteg 
- https://0xrick.github.io/lists/stego/

```sh
binwalk ransomwared.png
# 0             0x0             PNG image, 1344 x 896, 8-bit/color RGBA, non-interlaced
# 2767          0xACF           Zlib compressed data, default compression

exiftool ransomwared.png

strings ransomwared.png | less
```

https://stegonline.georgeom.net/upload set to blue 5 bitplane, saved as `ransomwared-blue5.png`

extracted text using https://brandfolder.com/workbench/extract-text-from-image

```txt
01010100 01101000 01101001 01110011 00100000 01110010 01100001 01101110 01110011 01101111 01101101 01110111 01100001 01110010
01100101 00100000 01100010 01110010 01101111 01110101 01100111 01101000 01110100 00100000 01110100 01101111 00100000 01111001
01101111 01110101 00100000 01100010 01111001 00100000 01101101 01101001 01110010 01110110 01100101 01100001 01101100 00101110
```

cyberchef from bin

```txt
This ransomware brought to you by mirveal.
```

`flag{mirveal}`
