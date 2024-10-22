# System Info

The malware that was ran on Garry’s machine gathered system information. 
We suspect that this information was saved on the system somewhere. 
Provide the full filepath to the file where DEADFACE saved system information.

Submit the flag as flag{path\to\file}. Example: flag{C:\Windows\System32\file.txt}

## Solution

Use dump from right-time

```sh
python3 vol.py -f ~/coding/repos/ctf/deadface-ctf-2024/phantom-operators/right-time/physmem.raw windows.pslist.PsList
```

winupdate.exe pid 8460

```sh
python3 vol.py -f ~/coding/repos/ctf/deadface-ctf-2024/phantom-operators/right-time/physmem.raw windows.handles --pid 8460


python3 vol.py -f ~/coding/repos/ctf/deadface-ctf-2024/phantom-operators/right-time/physmem.raw -o ~/coding/repos/ctf/deadface-ctf-2024/phantom-operators/system-info windows.memmap --dump --pid 8460

```

flag{C:\Users\garry\Downloads\update} - nope

C:\Users\garry\AppData\Local\Temp
C:\Windows\Temp\sysinfo.txt

`flag{C:\Windows\Temp\sysinfo.txt}`
