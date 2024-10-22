# Wild Wild West

Woah, our network has been lighting up like the fourth of a July on steroids, I tell you HWHAT. 
Now, given that we had a user call in complaining about weird stuff happening, 
I think it is about time you cowboy up and figure out what is happening in our here network.

Submit the flag as flag{flag-text}.

Download PCAP (394KB)
SHA1: e6959efe4522d92aa18c8ea15d8614fcfbdaee59

## Solution

```sh
wireshark 
```

strange - 3473	156.620456	10.10.34.2	10.10.34.255	NBNS	92	Name query NB WPAD<00>	

UDP streams
2887	118.129212	10.10.34.2	10.10.34.3	KRB5	271	KRB Error: KRB5KDC_ERR_PREAUTH_REQUIRED	
flag{kerbrute_finding_users}