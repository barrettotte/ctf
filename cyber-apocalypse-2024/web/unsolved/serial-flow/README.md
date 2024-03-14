# serial-flow

SerialFlow is the main global network used by KORP, you have managed to reach a root server web interface by traversing KORP's external proxy network. Can you break into the root server and open pandoras box by revealing the truth behind KORP?

## Solution

https://youtu.be/EGItzKCxTdQ?si=F8KvyV_phegOHEF9&t=1129

flask session + memcached allows command injection - https://btlfry.gitlab.io/notes/posts/memcached-command-injections-at-pylibmc/

injection is done from cookie `session=UUID` when making request

when it looks up value in memcached db, it unserializes a pickle object. Which we can use to get shell
