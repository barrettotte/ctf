# Revioli

Can you unlock the secret formula?

## Solution

`revioli`

```sh
file revioli                                                                                           master!?
# revioli: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=779286f1278a23eeb1c727e7bfb8804993ef4b81, for GNU/Linux 3.2.0, not stripped

strings revioli | less
# ITALY_%s
# PCTF{%s}
# Enter-a the password-a: 
# Congratulations! The flag is: %s
# No toucha my spaget!

strace ./revioli

ltrace ./revioli 
# snprintf("PCTF{ITALY_011235813213455891442"..., 256, "PCTF{%s}", "ITALY_01123581321345589144233377"...) = 38
# printf("Enter-a the password-a: ")

# PCTF{ITALY_01123581321345589144233377}
```
