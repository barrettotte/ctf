# eclairs

Apologize for the lack of flavortext :)

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Cryptography/Eclairs/writeup

encrypt 2 x to recover N
since y^2 = x^3 + ax + b thus b = y^2 - x^3 - ax
then we can use franklin reiter to recover a and b using only a single point
after recovering a and b we can then solve the captcha and get the flag
encrypt the flag with 3 different modulus and find the root using crt
