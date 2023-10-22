# host-busters-1

Turbo Tactical has gained access to a DEADFACE machine that belongs to `gh0st404`. 
This machine was used to scan one of TGRI’s websites. 
See if you can find anything useful in the `vim` user’s directory.

On a side note, it’s also a good idea to collect anything you think might be useful in the future for going after DEADFACE.

Submit the flag as flag{flag_here}.

`vim@gh0st404.deadface.io`

Password: `letmevim`

## Solution

```sh
ssh vim@gh0st404.deadface.io

# server: 0.0.0.0
# key: deadface

# :r!whoami
# vim

# :r!ls
# hostbusters1.txt

# :r!cat hostbusters1.txt
```

`flag{esc4P3_fr0m_th3_V1M}`
