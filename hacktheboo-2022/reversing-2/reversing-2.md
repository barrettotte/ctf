# Reversing 2

```sh
file encodedpayload
# ELF, 32-bit, statically linked, no section header

strings encodedpayload
# long string...but what is it?

ltrace ./encodedpayload

chmod +x encodedpayload
strace ./encodedpayload


readelf -a encodedpayload

# entrypoint 0x8048054
```

```sh
# gdb

gdb encodedpayload

set disassembly-flavor intel
starti

/x16i 0x8048054
```


spent hours wondering why the binary was stuck...

dude it was docker using the 1337 port. strace shows a connect to 127.0.0.1:1337

closed container, worked...flag in strace log


