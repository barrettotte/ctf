# kraken

"it's just wireguard over websockets with http being sent over that, and you have to fool the server to think you're localhost"


```
so kraken when viewing the file it'd open a websocket connection and tunnel wireguard through it through which it'd send a http request 
for the file you wanted to view
and when opening the websocket connection you'd specify your wg public key as well as your "public ipv6 address" 
used for connection, and you had to spoof the address to be a localhost one to bypass the "Remote access to this file is 
disabled" which could be done with ::ffff:127.0.0.1 which represents a localhost address

this was doable by either:
- reimplementing the entire thing to essentially recreate the client and do requests there (what I did)
- hooking/replacing the js randomvalues function which was used to generate the ipv6 address and return values to represent 
that localhost address (what the author did)
```