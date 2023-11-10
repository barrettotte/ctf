# leakin-park

For your final exercise, you aimed to create the spookiest encryption algorithm that bridges the human and ghost worlds. 
You chose RSA with a unique twist on prime generation. 
However, as a friend of the humans, your objective is to create something with a backdoor for decryption. 
You believe you've designed a solution that will deceive the Ghost Academy committee. 
Can you create a proof of concept to share with the humans?

## Solution

https://tig3rpuppet.blog/2023/10/28/hack-the-boo-2023-writeups/#leakin_park

```txt
It seems the goal is to figure out what p and q might be, which will allow us to reverse the RSA encryption.

The factors function returned an array of size 8 with random prime numbers less than 256.
```

...this is over my head...not going to review. Hopefully I study some cryptography soon...
