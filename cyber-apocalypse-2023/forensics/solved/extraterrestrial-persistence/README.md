# extraterrestrial-persistence

**SOLVED**

> There is a rumor that aliens have developed a persistence mechanism that is impossible to detect. 
> After investigating her recently compromised Linux server, Pandora found a possible sample of this mechanism. 
> Can you analyze it and find out how they install their persistence?

use cyberchef on base64 string in `persistence.sh`

```txt
[Unit]
Description=HTB{th3s3_4l13nS_4r3_s00000_b4s1c}
After=network.target network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes

ExecStart=/usr/local/bin/service
ExecStop=/usr/local/bin/service

[Install]
WantedBy=multi-user.target
```

`HTB{th3s3_4l13nS_4r3_s00000_b4s1c}`
