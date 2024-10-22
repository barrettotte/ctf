# Missing Persons

Your brother and private investigator, Jake Grahambell, was working on a high-profile case when he mysteriously disappeared two weeks ago. The last time you spoke, he mentioned traveling to a remote location and hinted at being in some kind of trouble. There have been rumours spreading in GhostTown about his disapearance as well. Can you piece together the clues and use your OSINT skills to uncover what happened to your brother?

Submit the flag as flag{flagtext}.

## Solution

scanning github repos
https://ghosttown.deadface.io/t/scanning-github-repos/55/4


https://ghosttown.deadface.io/t/dumping-the-world/61

Hacks go BRRRRRRRRRRR
Got this dudes SSN 035-55-4683
Name: Jake Grahambell
Birthday-04-02-1998
Address; 102 NotReal St, Smithstone, AL
Twitter: [x.com 87](http://x.com/OpticSeltzer69)

twitter
https://github.com/OpticSeltzer/Tictactoeeee
https://github.com/Adorable-Welcome-268



https://github.com/Adorable-Welcome-268/TheTruth
c8434c0c296d63bef55b7b2e4d75e6b665bfb93a

https://github.com/Adorable-Welcome-268/TRUTH
Oh shoot the IP address is 3.208.232.204

```sh
nc -vn 3.208.232.204 21
# Connection to 3.208.232.204 21 port [tcp/*] succeeded!
# 220 Microsoft FTP Service

ftp 3.208.232.204

sudo nmap -sV -p21 -sC -A 3.208.232.204
```
