# un-secure

Do you know what "unserialize" means? In PHP, unserialize is something that can be very dangerous, you know? 
It can cause Remote Code Execution. And if it's combined with an autoloader like in Composer, 
it can use gadgets in the autoloaded folder to achieve Remote Code Execution.

## Solution

```Dockerfile
# move flag to root directory with random name
RUN mv flag.txt $(cat /dev/urandom | head -c 32 | hex).txt
```

```php
require("vendor/autoload.php");
```

http://172.20.0.2

http://0.0.0.0:45678

`composer.json`

The PSR-4 and PSR-0 standards are two different PHP-FIG (PHP Framework Interoperability Group) standards for autoloading classes, and they offer different approaches for organizing and autoloading classes based on namespaces. PSR-4 is a more modern and efficient standard, while PSR-0 is an older, less efficient one

```php
if (isset($_COOKIE['cookie'])) {
    $cookie = base64_decode($_COOKIE['cookie']);
    unserialize($cookie);
}
```

need to create an object using the gadgets in `src/`

`GadgetThree/Vuln.php`

added php code to index.php

```php
```

`docker compose up -d --force-recreate --build web`

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/PHP.md




`O:17:"GadgetTwo\Echoers":1:{s:8:"*klass";N;}`

- `O` is object
- `17` is length of class name + namespace
- namespace\class
- `1` is number of properties object has
- `{` starts object properties
  - `s:8` is string length 8
  - `*klass` is property name, `*` means protected or private
  - `N` is for null value
- `}` closes properties

```php
    # O:17:"GadgetTwo\Echoers":1:{s:8:"*klass";N;}
$s = 'O:17:"GadgetTwo\Echoers":1:{s:5:"klass";i:42;}';
$o = unserialize($s);
echo var_dump($o) . '<br>';
```
