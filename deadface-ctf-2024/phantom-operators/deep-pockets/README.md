# Deep Pockets

Garry Sartoris had a CSV file of VIP clients on his machine that DEADFACE exfiltrated. 
TGRI wants us to confirm William Harrington’s account number to determine if his information was compromised. 
Submit William Harrington’s account number as the flag.

Submit the flag as flag{AAAA##############}.

## Solution

use pcap from big fish

```sh
# noticed xslx data in wireshark
# checked magic number hex - https://en.wikipedia.org/wiki/List_of_file_signatures

cp test.xlsx test.zip
unzip -o test.zip
```

`flag{RRNQ85158591854615}`

