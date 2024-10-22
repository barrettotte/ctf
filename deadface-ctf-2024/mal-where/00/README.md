# 00

The SOC team managed to quarantine an executable we think was left behind by DEADFACE actors. 
Unfortunately, they didn’t tell us what the password to the sample was. 
Can you figure out what the password is so we can start analyzing?

Submit the flag as flag{flag-text}

Download File (20KB)
SHA1: 453c474856ee2ac50e184a8feba5526c7736116f

## Solution

```sh
sudo apt-get install fcrackzip

fcrackzip -b -D -p /usr/share/wordlists/rockyou.txt -u 

# https://medium.com/@ujjawal.soni2002/cracking-a-password-protected-zip-file-using-john-the-ripper-f39e657cbfa8
/opt/john/run/zip2john Mal-Where\ is\ my\ mind.zip > zip.hash

/opt/john/run/john zip.hash
# infected

# flag{How_can_I_describe_my_emotions_at_this_catastrophe}
```
