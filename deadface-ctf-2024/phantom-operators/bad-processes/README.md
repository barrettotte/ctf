# Bad Processes

What is the PID of the malicious file that Garry ran after falling victim to the phishing scam?

Submit the flag as flag{PID}.

## Solution

https://ctf101.org/forensics/what-is-memory-forensics/

https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet

```sh
python3 vol.py -f ~/coding/repos/ctf/deadface-ctf-2024/phantom-operators/right-time/physmem.raw windows.pslist.PsList

# winupdate.exe pid 8460
```

I think its winupdate.exe from previous

`flag{8460}`
