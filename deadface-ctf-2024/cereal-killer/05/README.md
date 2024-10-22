# 05

This year, America's politicians are weighing in on the IMPORTANT issues...! As in, which spooky cereal is best?

President Donald Trump also has a favorite monster cereal, but it is secured by a password. 
As a test of your hacking mettle, oh great Turbo Tactical nerd, we need you to hack the program and gain access to the flag. Good luck!

Submit the flag as flag{flag-text}.

## Solution

https://github.com/D0pp3lgang3r/CTF-WU/blob/master/DEADFACE/wu.md#cerealkiller-05

```txt
we can simply do a KPA (known plaintext attack) with XOR on the link knowing first 5 bytes are https 
to get the key Br00t and grab all image link, we then compute hash of the image and we can decipher 
flag which has been ciphered by AES-GCM. see my solve script below :
```

```py
from pwn import *
import requests
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pathlib import Path

def decrypt_flag_with_aes_gcm(key, nonce_base64, ciphertext_base64):
    nonce = base64.b64decode(nonce_base64)
    ciphertext = base64.b64decode(ciphertext_base64)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

encrypted = [42, 6, 68, 64, 7, 120, 93, 31, 83, 17, 48, 23, 81, 92, 90, 46, 11, 68, 68, 27, 44, 30, 81, 82, 7, 108, 29, 66, 87, 91, 33, 23, 66, 85, 21, 46, 1, 31, 86, 6, 45, 29, 68, 82, 6, 45, 29, 68, 30, 30, 50, 23, 87]
encrypted_bytes = b""
for e in encrypted:
    encrypted_bytes+=e.to_bytes()

image_link = xor(encrypted_bytes, "Br00t") # l'image se récup avec https
with open("frootbroot.jpeg", "rb") as file:
    data = file.read()

key = hashlib.sha256(data).digest()
ivbase64 = "qHttv1t5TWZLDM4e"
ciphertext_base64 = "Tj/BJ+45Z45uRCFpuFOHirQI34ZC7bmtpCtJ3OE613fIxqrsZwIoLNSBXSjtPONFqZF3gC+4glh1Gyi2RBKZcuItH8s="

print(decrypt_flag_with_aes_gcm(key, ivbase64, ciphertext_base64)) # flag{Fr00t-Br00t-is-the-only-cereal-for-Prez-Trump!}
```


## Attempt

```sh
/opt/john/run/zip2john cerealkiller05.zip > zip.hash

/opt/john/run/john zip.hash
# d34df4c3

# converted jar to zip and decompiled class with http://www.javadecompilers.com/

java -jar cerealkiller05.jar
```

42, 6, 68, 64, 7, 120, 93, 31, 83, 17, 48, 23, 81, 92, 90, 46, 11, 68, 68, 27, 44, 30, 81, 82, 7, 108, 29, 66, 87, 91, 33, 23, 66, 85, 21, 46, 1, 31, 86, 6, 45, 29, 68, 82, 6, 45, 29, 68, 30, 30, 50, 23, 87
