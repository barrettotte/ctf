# small-steps

**SOLVED**

> As you continue your journey, you must learn about the encryption method the aliens used to secure their communication from eavesdroppers. 
> The engineering team has designed a challenge that emulates the exact parameters of the aliens' encryption system, complete with instructions and a code snippet to connect to a mock alien server. 
> Your task is to break it.

```py
class RSA:

    def __init__(self):
        self.q = getPrime(256)
        self.p = getPrime(256)
        self.n = self.q * self.p
        self.e = 3

    def encrypt(self, plaintext):
        plaintext = bytes_to_long(plaintext)
        return pow(plaintext, self.e, self.n)
```

https://docs.python.org/3/library/functions.html#pow

(plaintext_long ^ e) mod p*q
(plaintext_long ^ 3) mod n

```md
# Hints

The implementation is textbook RSA, except for the value of `e`.
```

https://en.wikipedia.org/wiki/RSA_(cryptosystem)

"d is kept secret as the private key exponent."

Encryption:
c = m^e (mod n)

Decryption:
Alice can recover m from c by using her private key exponent d by computing 
c^d = (m^e)^d = m (mod n)
Given m, she can recover the original message M by reversing the padding scheme. 

`nc 46.101.73.33 30772`

```
The public key is:

N: 5948555947726318707067712055275123555980184727183255424912967504010379326734617597681828446457535063101277329836724582378402652388657654883252611947611993
e: 3
The encrypted flag is: 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
```

(m^3)^d = m (mod n)

https://crypto.stackexchange.com/questions/33561/cube-root-attack-rsa-with-low-exponent

https://crypto.stackexchange.com/questions/1448/definition-of-textbook-rsa

Textbook RSA

public key encrypt:  C = M^e (mod N)
private key decrypt: C^d = M (mod N)


https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Using_the_Chinese_remainder_algorithm

https://crypto.stackexchange.com/questions/55941/breaking-rsa-using-chinese-remainder-theorem


```sh
python3 crypto_small_steps/solver.py REMOTE HOST=46.101.73.33:30772

# 1
# n=8722287678477553937647526125653222515289998148105612529297791849753568527641108107971718877947159755077344866153273130937367284581036627277762676002889577
# c=70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053

# 2
# n=4845460036350840943192360186590297824295403329906191028547002090114416844222511233515978683212376516974422024989718844568349043927709901404582115803493857
# c=70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053

# 3
# n=12356132125241099869961263780605445843686002407983271463082864794395899829440642388080969813450171464600303109426325770896690753450410033935021562812888293
# c=70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
```

https://github.com/RsaCtfTool/RsaCtfTool

```sh
pip3 install libnum
python3 flag.py
```

`HTB{5ma1l_E-xp0n3nt}`
