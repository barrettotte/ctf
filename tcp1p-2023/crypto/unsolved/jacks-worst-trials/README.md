# jacks-worst-trials

Jack, a web developer intern, is asked to make a website for his trial probation in his company. 
Some say a treasure will be given to anyone who is able to log in as an admin, 
although not a single person is assigned as an admin by Joe, not even himself.

Note: He's a bit old-fashioned, so it's not surprising that he uses outdated components for his website.

## Solution

A JWT key confusion attack on pyjwt 1.5.0 (CVE-2017-11424) that allow attacker to use public key on RS256-JWT validation by re-encoding the system's public key and specify it as HS256-JWT

Summary: No matter how user registered an account, admin flag will always set as false. The objective is to change it to admin true and get the flag. Upon login, user receive a jwt token located at cookie.

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Cryptography/Jack's%20Worst%20Trials/writeup
