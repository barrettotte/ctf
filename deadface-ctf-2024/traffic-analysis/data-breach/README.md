# Data Breach

We suspect an internal employee is leaking sensitive information, but the source remains unclear. 
We've captured network traffic for analysis. 
Your mission is to investigate the data and locate the hidden flag.

Can we count on your expertise to track it down?

Submit the flag as flag{flag-text}.

Download PCAP (342KB)
SHA1: 48744d0b724fc30f660a7953b5e974320b60a47c

## Solution

```sh
unzip -o databreach.zip
wireshark databreach.pcapng
```

3721	282.474122	10.10.34.2	10.10.34.3	HTTP	1060	HTTP/1.1 200 OK  (text/html)	

Not-Suppose-To-Be-Here: flag{Information_disclosure_in_the_head}