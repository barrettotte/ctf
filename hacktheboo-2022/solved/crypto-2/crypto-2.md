# Crypto 2 - Fast Carmichael

what is this even asking

```python
# main; ticket to flag
if _isPrime(p) and not isPrime(p):
    sendMessage(s, FLAG)
    # local _isPrime false and Crypto.Util.number.isPrime true

# _isPrime()
# the other check looks like garbage, need to manipulate this:
if not millerRabin(p, 300):
    return False
```

title includes carmichael, so need carmichael numbers


## Carmichael numbers

https://en.wikipedia.org/wiki/Carmichael_number

- have at least three positive prime factors

