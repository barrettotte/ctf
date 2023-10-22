# host-busters-2

Now that you’ve escaped out of `vim`, scope out and characterize the machine. 
See if there are any other flags you can find without having to escalate to another user.

Submit the flag as `flag{flag_here}`.

`vim@gh0st404.deadface.io`

Password: `letmevim`

## Solution

I was right there!

```
kris@m1pro:~ $ ssh vim@gh0st404.deadface.io
vim@gh0st404.deadface.io's password:

vim@7e83c1271fbe:~$

vim@7e83c1271fbe:~$ netstat -ptanu
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
udp        0      0 0.0.0.0:9023            0.0.0.0:*                           8/srv
vim@7e83c1271fbe:~$ nc -u localhost 9023

flag{Hunt_4_UDP_s3rv3r}
```


## My Attempt

```sh
ssh vim@gh0st404.deadface.io
```

https://zacheller.dev/text-editor-jail

```txt
:set shell=/bin/bash
:shell
```

```sh
find / -type f -name '*flag*' 2>/dev/null
find . -type f -print | xargs grep "flag{"
find . -type f -perm 0777 -print
```

```sh
find / -type f -readable ! -path "/sys/*" 2>/dev/null
# /home/vim/.bashrc
# /home/vim/.profile
# /home/vim/.bash_logout
# /home/vim/.viminfo
# /home/vim/hostbusters1.txt
# /home/spookyboi/.bashrc
# /home/spookyboi/.profile
# /home/spookyboi/.bash_logout
# /home/spookyboi/.keys/spookyboi-public.pem
# /home/spookyboi/.keys/spookyboi-priv.pem
# /home/gh0st404/.bashrc
# /home/gh0st404/.profile
# /home/gh0st404/.bash_logout
# /home/gh0st404/.keys/gh0st404-priv.pem
# /home/gh0st404/.keys/gh0st404-public.pem
# /home/gh0st404/tgri-alive.xml
# /home/gh0st404/config
# /home/gh0st404/id_rsa
# /home/gh0st404/tgri-scan.xml
# /home/mort1cia/.bashrc
# /home/mort1cia/.profile
# /home/mort1cia/.bash_logout

find /etc -type f -readable 2>/dev/null
```

```sh
# suid binaries

find / -user root -perm -4000 -print 2>/dev/null
# /usr/bin/mount
# /usr/bin/passwd
# /usr/bin/gpasswd
# /usr/bin/umount
# /usr/bin/newgrp
# /usr/bin/su
# /usr/bin/chfn
# /usr/bin/chsh
# /usr/bin/sudo
# /usr/lib/dbus-1.0/dbus-daemon-launch-helper
# /usr/lib/openssh/ssh-keysign
```

https://gtfobins.github.io/

can't find anything...

Make sure you are really characterizing the target! There is some good info to be found rather easily, so if you are down a rabbit hole, back up and reassess

have `nmap` installed?

```sh
nmap -A 0.0.0.0 -vv
nmap -A 0.0.0.0 -vv --privileged
```


interesting: docs.techglobalresearch.com

```sh
nmap -v -sn 10.0.0.0/25
```

https://book.hacktricks.xyz/linux-hardening/privilege-escalation#system-information

echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > /home/spookyboi/overwrite.sh

```
It seems that everybody is treating Host Busters 2 like a pwn challenge when it is actually a forensics challenge. 
Rather than enumerating the system for vulnerabilities and gaining root, characterize what the system is doing 
and try to find unique things going on
```


```txt
vim@968dfbf49ee1:~$ cat /usr/bin/start
#!/bin/sh
/usr/bin/srv &
#/etc/init.d/ssh start
/bin/vim /home/gh0st404/config
exit 0
```

```
netstat -tulpn

tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 0.0.0.0:9023            0.0.0.0:*                           8/srv
```

```sh
fuser 9023/udp
# 8

ls -l /proc/8/
```
