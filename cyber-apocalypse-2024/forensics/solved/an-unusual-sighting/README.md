# an-unusual-sighting

As the preparations come to an end, and The Fray draws near each day, our newly established team has started work on refactoring the new CMS application for the competition. 
However, after some time we noticed that a lot of our work mysteriously has been disappearing! 
We managed to extract the SSH Logs and the Bash History from our dev server in question. 
The faction that manages to uncover the perpetrator will have a massive bonus come competition!

## Solution

`nc 83.136.252.250 30901`


```txt
What is the IP Address and Port of the SSH Server (IP:PORT)
100.107.36.130:2221

What time is the first successful Login
2024-02-13 11:29:50

What is the time of the unusual Login
2024-02-19 04:00:14

What is the Fingerprint of the attacker's public key
OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4

What is the first command the attacker executed after logging in
whoami

What is the final command the attacker executed before logging out
./setup

HTB{B3sT_0f_luck_1n_th3_Fr4y!!}
```