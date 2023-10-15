# cherry-leak

Why did the RSA challenge go to the fruit stand? To cherry-pick it's leaks.

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Cryptography/Cherry%20Leak/writeup

Doing some math we can recover a multiple of q 
suppose `x = p - q` and `y = p % q p = kq + y x + q = kq + y x - y = (k-1)q` 

by getting new p, we can do it again and find q by GCD 

notice that the flag is relatively small, that is, FLAG < q 
so we can simply find d using inverse of e mod q-1 and still be able to decrypt the flag

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Cryptography/Cherry%20Leak/writeup/solve.py
