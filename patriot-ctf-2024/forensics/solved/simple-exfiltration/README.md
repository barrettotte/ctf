# Simple Exfiltration

We've got some reports about information being sent out of our network. 
Can you figure out what message was sent out

## Solution

4139

TLSv1.2 packets seem weird...not sure what to do with this

8af300022558e64649b62c48e788d34a240f2700b8eabbfe9ab7feac87408320c72e
c07ba524a409fcb32fd1485fbcf37ccb7628aedb0797e8ad47e7fca1b5f424a68273
433805cf2d274046e25cbad31cb5328677116638397f1ebd292ce168d84809132247
7a0dec3289075bc46e95cbd8d1c68261290472

719f3cf234dbdcecbc876380579cd1521485b3
63e5b209bf902f66f0d0728a3fef421e68785f

ICMP packets?
extract TTL? It seems to be changing

```sh
python3 solve.py
# pctf{time_to_live_exfiltration}
```
