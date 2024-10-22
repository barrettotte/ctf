# 01

DEADFACE has created a site http://deadbrowse.deadface.io:3000 and a browser that goes along with it. 
Figure out how to access the site!

Submit the flag as flag{flag-text}

Download File (5KB)
SHA1: 4a7e106c9fcb0a22121191b5196803e98bbf3483

## Solution

https://fluxh4cks.medium.com/deadface-ctf-dead-browse-1-reverse-engineering-challenge-write-up-9be8a0231814

## Attempt

```sh
./dead_browse --url=http://deadbrowse.deadface.io:3000 --auth-key=my_secret_key --check-user-key
```
