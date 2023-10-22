# cereal-killer-03

`deephax` is rather paranoid about sharing personal information. 
He has a favorite cereal, but he doesn’t want to share that information with the government. 
You’re going to have to work at this one a little bit.

## Solution

Cutter is apparently good for reversing Go binaries

https://cereal.lyttonlabs.org is in the binary somewhere

then use `dirbuster` for site enumeration and find `.txt` file

## My Attempt

```sh
strings re03.bin
# 9cttbgipkAEjKOEwNzn9/uJMsXykCqMjRk_dxCYaO/OYKNT6dVi-IbRPzC8BWz/rTLFFm8l1lPvK_AIPCho

file re03.bin
# re03.bin: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, 
# Go BuildID=9cttbgipkAEjKOEwNzn9/uJMsXykCqMjRk_dxCYaO/OYKNT6dVi-IbRPzC8BWz/rTLFFm8l1lPvK_AIPCho, with debug_info, not stripped
```
