# 2 - Short Term

Now that you've accessed deephax's machine, see if you can find the flag associated with Hostbusters 2.

Submit the flag as flag{hostbusters2_flagtext}.

## Solution

Sigh...

```sh
ls -al /tmp
cat /tmp/.flag2.txt

# next time do this
find / -name '*flag*' 2> /dev/null
```

## Attempt

Host: deephax@deephax.deadface.io
Username: deephax
Password: D34df4c32024$

```sh
printenv
# flag3=flag{hostbusters3_ff07d6fb5ee992f6}

ps aux

find / -name 'flag*'

uname -a

cat /opt/sendit/.config.conf 
# modified by lillith?

# {
#   "host": "c2.deadface.io",
#   "port": 1516,
#   "path": "/opt/sendit"
}

find / -perm -4000 -type f 2>/dev/null
# /usr/bin/readlog
# /usr/bin/sudo
# /bin/bbsuid

cat /usr/local/bin/start.sh 
# cat: can't open '/usr/local/bin/start.sh': Permission denied

find . -type f -print | xargs grep "flag"

/usr/bin/readlog -f /proc/1/environ
```
