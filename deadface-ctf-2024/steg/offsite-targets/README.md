# Offsite Targets

lamia415 sent an image to daem0n with secret information about who or what they are building a campaign against. 
Turbo Tactical wants to lean forward on this and prepare any individuals or companies that might be targeted by DEADFACE. 
Find out what the hidden message is and submit the flag.

Submit the flag as: flag{text_here}.

## Solution

```sh
file img...

strings -n 7 -t x img20240803.jpg | less

binwalk -Me img20240803.jpg

steghide extract -sf img20240803.jpg

gzip -d secret.txt.gz
```

https://ghosttown.deadface.io/t/steganography-script-update/50

```txt
I’ve finally managed to refine my steganography script to embed messages in MP3 files. Originally, I had a working version for WAV files, but the file sizes were too large and inconvenient. Embedding in MP3 files initially caused issues with the ID3 headers, but I’ve now resolved those problems. The script ensures the message is hidden in the least significant bits without corrupting the audio quality or metadata. Anyone interested in testing it out or providing feedback?
```

https://ghosttown.deadface.io/t/secret-message-enclosed/59/4
d34df4c3

flag{S0c14l_3ng1neer1ng_1nt3l_fr0m_0ff-s1t3}

