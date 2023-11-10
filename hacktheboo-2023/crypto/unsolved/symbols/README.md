# symbols

The exam season is coming up, and you have to study the encryption used in malwares. 
The class structure involves the professors providing you with an encryption function, and your task is to find a way to decrypt the data without knowing the key. 
Practicing this will lead you to becoming proficient in cryptography, making data recovery by humans nearly impossible.

## Solution 1

https://tig3rpuppet.blog/2023/10/28/hack-the-boo-2023-writeups/#symbols


```txt
The trick here is to analyze the r variable and realize that it is going to be an even number whenever the bit is 0, 
and an odd number whenever the bit is 1. 
This means that each item of our ciphertext takes the form c = 1337 ^ r mod p and if we can determine whether r is odd or even, 
then that tells us the value of the corresponding bit in the plaintext.

if r is even, 1337 ^ r is a perfect square, and c is what’s know as a quadratic residue.

https://en.wikipedia.org/wiki/Quadratic_residue
```

```py
from pwn import *
 
p = 307163712384204009961137975465657319439
g = 1337
 
# This is correct if it is only ever run on a prime number, which `p` is.
def factor(n):
    return [(n, 1)]
 
def power_mod(base, exp, mod):
    return pow(base, exp, mod)
 
def peel(a, p):
    # Returns (k, b) such that a = p^k * b and b is minimal.
    if a == 0: return (1, 0)
    k = 0
    while a % p == 0:
        k += 1
        a = a // p
    return (k, a)
 
def is_quadratic_residue(a, n):
    for (p, e) in factor(n):
        (k, b) = peel(a % p**e, p)
        if b == 0: continue
        if k % 2: return False
        if p == 2:
            if e == 1: continue
            if b % 4 != 1: return False
            if e >= 3 and b % 8 != 1: return False
        else:  # Euler's criterion
            if power_mod(b, (p - 1)//2, p) != 1:
                return False
    return True
 
def main():
    with open('./output.txt', 'r') as f:
        output = eval(f.read())
 
    s = ''.join(map(lambda c: ('0' if is_quadratic_residue(c, p) else '1'), output))
    i = int(s, 2)
    flag = pack(i, endianness='big', word_size='all')
    print(flag)
 
if __name__ == '__main__
```

## Solution 2

```py
# solver.sage

# The key idea is that you can take advantage of the fact that modular exponentiation with an even exponent always results in a quadratic residue, 
# while modular exponentiation with an odd exponent always results in a non-quadratic residue. 
# You can use this property to efficiently determine whether r is even or odd.

from Cryptodome.Util.number import long_to_bytes
from output import encrypted_message

p = 307163712384204009961137975465657319439
K = Zmod(p)
g = K(1337)

dec_list = []

for b in encrypted_message:
    result = power_mod(int(b), (p - 1) // 2, p)
    if result == 1:
        dec_list.append(0)
    else:
        dec_list.append(1)

print(long_to_bytes(int(''.join(map(str, dec_list)), 2)))
```

## Attempt

https://github.com/barrettotte/ctf/blob/master/hacktheboo-2022/solved/crypto-1/decrypt.py#L14

$i = g^x (mod\ p)$

$x = \log_g(i) (mod\ p)$

brute force - no, p too large

baby-step giant-step algorithm - https://gist.github.com/0xTowel/b4e7233fc86d8bb49698e4f1318a5a73, p too large

Pollard's Rho algorithm , p might be too large
- https://github.com/markusju/pollard-rho/blob/master/pollard_rho.py
- https://asecuritysite.com/encryption/log_rho?val1=12&val2=7&val3=41

Index Calculus Algorithm
- https://github.com/david-r-cox/pyDLP


- https://en.wikipedia.org/wiki/ElGamal_encryption
- https://minyak128.medium.com/elgamal-encryption-explained-38e9efda1a0f


https://github.com/bobmitch23/discrete-log/blob/master/python/discrete_log/pohlig_hellman.py

https://pypi.org/project/pycryptodome/

```sh
sudo apt install sagemath
conda install sage

sage --python solve.py 
# still no dice...
```
