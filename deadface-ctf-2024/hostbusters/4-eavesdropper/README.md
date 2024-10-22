# 4 - Eavesdropper

## Solution

https://rmi78.github.io/posts/Deadface-CTF/#flag-4-eavesdroppers

```sh
ps -a
# root - /usr/local/bin/start.sh
# root - /usr/local/bin/usrv

netstat
# 0.0.0.0:2342

nc -u 127.0.0.1 2342
# flag
```
