# perfect-synchronization

**SOLVED**

> The final stage of your initialization sequence is mastering cutting-edge technology tools that can be life-changing. 
> One of these tools is quipqiup, an automated tool for frequency analysis and breaking substitution ciphers. 
> This is the ultimate challenge, simulating the use of AES encryption to protect a message. 
> Can you break it?

https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation

key=16
salt=15

each block 32 bytes

1 byte of padding?

https://www.youtube.com/watch?v=unn09JYIjOI

aes = encrypt(salt + key) + pad ?

`sort output.txt | uniq -c | sort -bgr`

manually replaced each occurrence of block with find and replace all
using alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ_{} and a whitespace

used https://quipqiup.com/ patristocrat solver

`HTB{A SIMPLE SUBSTITUTION IS WEAK}`

must have mixed up space and underscore

`HTB{A_SIMPLE_SUBSTITUTION_IS_WEAK}`
