# Crypto 4 - Whole Lotta Candy

uhhh i guess pwntools to start?

```txt
https://www.highgo.ca/2019/08/08/the-difference-in-five-modes-in-the-aes-encryption-algorithm/

# ECB
  - Electronic Code Book
  - weak; not recommended

# CBC
  - Cipher Block Chaining
  - random iv 16 bytes

# CFB
  - Cipher FeedBack
  - random iv 16 bytes

# OFB
  - Output FeedBack
  - random iv 16 bytes

# CTR
  - Counter
  - IV value of counter


# encrypt.py -> CTR, shouldnt counter be incremented?
#   in other words, its same key each time? nope stateful, incremented each call

# AES-CTR Reused Key Weakness: https://www.youtube.com/watch?v=Gtfr1dBGzHg

# CTR and ECB both reuse keys...can we use either? Aparently not, TODO: why not?

see exploit.py

```

