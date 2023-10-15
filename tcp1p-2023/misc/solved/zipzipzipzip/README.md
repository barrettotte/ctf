# zipzipzipzip

unzip me pls

## Solution

nested password-protected zip files...25K of them

`solve.py` -> last unzip has flag `TCP1P{1_TH1NK_U_G00D_4T_SCR1PT1N9_botanbell_1s_h3r3^_^}`

## Alternative Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/blob/main/Misc/zipzipzipzip/solve.sh

```sh
#!/bin/bash

NUM=25000
FILENAME="zip"
PASS_FILE="password.txt"

# extract from archive NUM times
for ((i=$NUM; i > 0; i--)); do
  FILE="$FILENAME-$i.zip"

  password=$(cat "$PASS_FILE")
  yes | unzip -oP "$password" "$FILE"
  rm "$FILE"
done
```
