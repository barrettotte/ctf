# Crypto 1 - Gonna-Lift-Em-All

yikes

## References

- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses
- https://www.crypto-it.net/eng/theory/modular-arithmetic.html
- https://en.wikipedia.org/wiki/Modular_arithmetic#Properties

## Math

```txt
known: p, g ,h ,c_1, c_2

modular arithmetic has no division, use multiplicative modular inverse

h = g^x (mod p)
s = h^y (mod p)
c_1 = g * y (mod p)
c_2 = m * s (mod p)

y = (c_1 * g^-1) (mod p)

m = (c_2 * s^-1) (mod p)
```
