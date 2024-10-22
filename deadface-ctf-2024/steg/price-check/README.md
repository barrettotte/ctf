# Price Check

DEADFACE has been hacking random people all over town and no one can seem to figure out what they are doing. 
All we know at this time is that the most recent site that was hit was Otto’s Grocery Store. 
Oddly, only the customers are being affected and not the company’s network. 
What is happening? 
They hired our firm to sniff out the attack and we successfully captured a strange file being sent across the guest WiFi. 
We believe this is the primary attack vector, and we’ve heard some victims mention that they had to “scan” something - 
maybe it is in the wrong format? 
Can you figure out how this file is being used in the attack to reveal the flag?

Submit the flag as flag{flag_text_here}.

Download File (2.5KB)
SHA1: 213f1e381da74815b8c347f3cc1c28a8c6675085

## Solution

Some sort of barcode scan format?

https://github.com/mar232320/ctf-writeups/blob/main/wreck2022/barcode/barcode.md

actually a qr code

```sh
python3 solve.py

# flag{that_will_be_five_dollars}
```
