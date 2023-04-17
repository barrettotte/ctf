# Reversing - Cult Meeting

opened `meeting.sh` in IDA

```asm
lea     rsi, s2         ; "sup3r_s3cr3t_p455w0rd_f0r_u!"
```

```sh
echo 'sup3r_s3cr3t_p455w0rd_f0r_u!' | nc $TARGET_IP $TARGET_PORT
```


https://github.com/Gallopsled/pwntools#readme

messed around with pwntools awhile, for some reason text wasn't showing up in terminal
and it took me forever to figure out how to fix it.
