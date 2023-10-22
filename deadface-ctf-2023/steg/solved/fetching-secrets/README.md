# fetching-secrets

This image was found on Ghost Town. 
Looks like one of DEADFACE’s newest members is new to steganography.
See if you can find any hidden information in this image. 
Knowing information about the image may help to reveal the flag.

Submit the flag as: flag{flag_text}.

https://cyberhacktics.sfo2.digitaloceanspaces.com/DEADFACECTF2023/Challenges/steg/steg01/cyberdog.jpg

## Solution

https://stylesuxx.github.io/steganography/

```sh
binwalk cyberdog.jpg
exiftool cyberdog.jpg

steghide extract -sf cyberdog.jpg
# i dont know the password
```

https://github.com/zed-0xff/zsteg -> not for jpg

https://0xrick.github.io/lists/stego/


"Knowing information about the image may help to reveal the flag."

https://ghosttown.deadface.io/t/steganography-techniques/115

https://github.com/RickdeJager/stegseek

```sh
stegseek cyberdog.jpg /usr/share/wordlists/rockyou.txt
# kira

steghide extract -sf cyberdog.jpg -xf extracted

file extracted
# png

cp extracted extracted.png
```

`flag{g00d_dawg_woofw00f}`
