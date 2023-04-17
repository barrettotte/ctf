# Crypto 3 - Spooky RSA


see `solution.py`


## Math Notes

```txt
c_1 = (f^{e_1}(mod N)) + m (mod N) = (p^{e_1}(mod N)) + m (mod N)
c_2 = (f^{e_2}(mod N)) + m (mod N) = (p^{e_2}(mod N)) + m (mod N)

c_1 = p^{e_1}(mod N) = m (mod N)
c_2 = p^{e_2}(mod N) = m (mod N)

(c_1 - p^{e_1}(mod N))(mod n) = (c_2 - p^{e_2}(mod N))(mod N)

(c_1 - c_2)(mod N) = (c_2 - p^{e_2}(mod N)) (mod N)

c_1 - (p^{e_2}(mod N)) + m(mod N) = p^{e_1} - p^{e_2} (mod N)

(c_1 + m) (mod N) = p^{e_1} (mod N)

(c_1 - p^{e_1}) (mod N) = -m (mod N)

m = -c_1 + p^{e_1}

value must be non-negative...must have screwed up a sign somewhere

m = c_1 + p^{e_1} ; worked!
```
