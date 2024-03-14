# recovery

We are The Profits. During a hacking battle our infrastructure was compromised as were the private keys to our Bitcoin wallet that we kept.
We managed to track the hacker and were able to get some SSH credentials into one of his personal cloud instances, can you try to recover my Bitcoins?
Username: satoshi
Password: L4mb0Pr0j3ct
NOTE: Network is regtest, check connection info in the handler first.

## Solution

https://youtu.be/EGItzKCxTdQ?si=jZhsICW6-q8Egy2X&t=5627

ssh to box with given credentials

cat electrum wallet seed

`ps aux` machine running electrs, bitcoind, electrum wallet

use wallet seed to create/recover wallet

send btc to challenge address
