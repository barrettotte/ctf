# Big Fish

TGRI employee Garry Sartoris fell for a phishing attack recently. 
It’s hard to say what DEADFACE was after, but Turbo Tactical needs your help looking through the attack artifacts. 
Take a look at this PCAP and submit the attacker’s IP address.

Submit the flag as flag{IP Address}.

## Solution

```sh
wireshark phantom.pcap
```

14069	173.243460	45.55.201.188	10.65.201.100	HTTP	1011	HTTP/1.1 200 OK  (application/x-msdownload)	
nc.exe

`flag{45.55.201.188}`

