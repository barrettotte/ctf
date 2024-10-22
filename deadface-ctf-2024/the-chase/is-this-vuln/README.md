# Is This Vulnerable

DEADFACE is at it again! We have started to catch wind of a big attack in the works and we have to stop them before they wreak havoc again this year. No! This year DEADFACE is going down big time. 
One of our threat intelligence analysts has been hard at work and thinks they have stumbled onto a breadcrumb trail in GhostTown. 
Can you figure out how DEADFACE got their initial access into our environment?

Welcome to The Chase challenge series.

Submit the flag as flag{flag}.

## Solution

Use john with a different wordlist, I forget which one...

## Attempt

https://ghosttown.deadface.io/t/yes-it-is-vulnerable/70

```txt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsIm5vbmNlIjoiIn0.eyJpc3MiOiJ0dXJib3RhY3RpY2FsLm5ldCIsImV4cCI6IjE0NTA2NTkxMDIiLCJ1cG4iOiJjZm9kZXJhIiwiZnVsbF9uYW1lIjoiQ2xhaXIgRm9kZXJhIiwidXNlcm5hbWUiOiJDRm9kZXJhOTEiLCJwaG9uZV9udW1iZXIiOiIiLCJqdGkiOiJmdGlkMjM0MmEtMzI0M2QtMjM0My1kMzR5OHlnZmZlIiwic3R1ZmYiOjExMjIyLCJncm91cHMiOlsibG93X2FkbWluIiwicmVtb3RlX3VzZXIiLCJsYWJ0ZWNoIl0sIm9yZyI6IlR1cmJvVGFjdGljYWwiLCJzdWJfb3JnIjoiR3JvdXBfRCIsIm5idCI6NTc1NDczNzU0ODI5NTI3NTAwMDAsImxkZV9zIjpbeyJhc3RhdHVzIjoibnVsbCIsImJzdGF0dXMiOiJudWxsIiwiY3N0YXR1cyI6InZhbGlkIiwiZHN0YXR1cyI6Im51bGwifV19.kQKRFPLj_SqVeEiBjfKi7FKOEVoV71JgdFRxDTjp7TQ
```

https://blog.pentesteracademy.com/hacking-jwt-tokens-bruteforcing-weak-signing-key-johntheripper-89f0c7e6a87

https://security.stackexchange.com/questions/262106/crack-jwt-hs256-with-hashcat

```sh
/opt/hashcat/hashcat -m 16500 -a 0 ~/jwt.txt /usr/share/wordlists/rockyou.txt 

# clBuildProgram(): CL_BUILD_PROGRAM_FAILURE

~/Downloads/hashcat/hashcat -m 16500 -a 0 ~/coding/repos/ctf/deadface-ctf-2024/the-chase/is-this-vuln/jwt.txt /usr/share/wordlists/rockyou.txt

sudo apt remove pocl-opencl-icd
sudo apt-get install libpocl2 -y

```

```sh
flask-unsign --wordlist /usr/share/wordlists/rockyou.txt --unsign --cookie 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsIm5vbmNlIjoiIn0.eyJpc3MiOiJ0dXJib3RhY3RpY2FsLm5ldCIsImV4cCI6IjE0NTA2NTkxMDIiLCJ1cG4iOiJjZm9kZXJhIiwiZnVsbF9uYW1lIjoiQ2xhaXIgRm9kZXJhIiwidXNlcm5hbWUiOiJDRm9kZXJhOTEiLCJwaG9uZV9udW1iZXIiOiIiLCJqdGkiOiJmdGlkMjM0MmEtMzI0M2QtMjM0My1kMzR5OHlnZmZlIiwic3R1ZmYiOjExMjIyLCJncm91cHMiOlsibG93X2FkbWluIiwicmVtb3RlX3VzZXIiLCJsYWJ0ZWNoIl0sIm9yZyI6IlR1cmJvVGFjdGljYWwiLCJzdWJfb3JnIjoiR3JvdXBfRCIsIm5idCI6NTc1NDczNzU0ODI5NTI3NTAwMDAsImxkZV9zIjpbeyJhc3RhdHVzIjoibnVsbCIsImJzdGF0dXMiOiJudWxsIiwiY3N0YXR1cyI6InZhbGlkIiwiZHN0YXR1cyI6Im51bGwifV19.kQKRFPLj_SqVeEiBjfKi7FKOEVoV71JgdFRxDTjp7TQ' --no-literal-eval


~/Downloads/hashcat/hashcat -m 16500 -a 0 ~/coding/repos/ctf/deadface-ctf-2024/the-chase/is-this-vuln/jwt.txt /usr/share/wordlists/SecLists-2023.2/Passwords/scraped-JWT-secrets.txt
```

https://github.com/ticarpi/jwt_tool

```sh
python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsIm5vbmNlIjoiIn0.eyJpc3MiOiJ0dXJib3RhY3RpY2FsLm5ldCIsImV4cCI6IjE0NTA2NTkxMDIiLCJ1cG4iOiJjZm9kZXJhIiwiZnVsbF9uYW1lIjoiQ2xhaXIgRm9kZXJhIiwidXNlcm5hbWUiOiJDRm9kZXJhOTEiLCJwaG9uZV9udW1iZXIiOiIiLCJqdGkiOiJmdGlkMjM0MmEtMzI0M2QtMjM0My1kMzR5OHlnZmZlIiwic3R1ZmYiOjExMjIyLCJncm91cHMiOlsibG93X2FkbWluIiwicmVtb3RlX3VzZXIiLCJsYWJ0ZWNoIl0sIm9yZyI6IlR1cmJvVGFjdGljYWwiLCJzdWJfb3JnIjoiR3JvdXBfRCIsIm5idCI6NTc1NDczNzU0ODI5NTI3NTAwMDAsImxkZV9zIjpbeyJhc3RhdHVzIjoibnVsbCIsImJzdGF0dXMiOiJudWxsIiwiY3N0YXR1cyI6InZhbGlkIiwiZHN0YXR1cyI6Im51bGwifV19.kQKRFPLj_SqVeEiBjfKi7FKOEVoV71JgdFRxDTjp7TQ


/opt/john jwt.txt -w=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256
```

