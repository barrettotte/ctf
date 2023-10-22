# host-busters-3

Continue characterizing the machine.
Is there any way you can escalate to a user that has permissions the `vim` user does not have? 
Find the flag associated with this user.

Submit the flag as `flag{flag_here}`.

`vim@gh0st404.deadface.io`

Password: `letmevim`

## Solution

https://ghosttown.deadface.io/t/initiate-scans-on-docs/110/5

```sh
cp /home/gh0st404/id_rsa ~/.ssh
chmod 600 ~/.ssh/id_rsa

ssh gh0st404@localhost
```

`flag{Embr4c3_th3_K3y_t0_5ucc355!}`
