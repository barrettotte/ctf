# roten

**SOLVED**

> The iMoS is responsible for collecting and analyzing targeting data across various galaxies. 
> The data is collected through their webserver, which is accessible to authorized personnel only. 
> However, the iMoS suspects that their webserver has been compromised, and they are unable to locate the source of the breach. 
> They suspect that some kind of shell has been uploaded, but they are unable to find it. 
> The iMoS have provided you with some network data to analyse, its up to you to save us.

HTTP POST /results_display.php 

```txt
Interesting packets

1008	66.434437	212.102.35.152	172.31.9.156	HTTP	2106	POST /map-update.php HTTP/1.1  (application/pdf)

1929	292.666144	146.70.38.48	172.31.9.156	HTTP	286	POST /map-update.php HTTP/1.1  (application/x-php)
looks like php eval used on 1929
```

downloaded php from http stream on 1929

`sudo apt-get install php`

`php obfuscated.php > shell.php`

flag is comment in `shell.php`
