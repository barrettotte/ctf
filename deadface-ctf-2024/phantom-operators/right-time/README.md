# Right Time

TGRI employee Garry Sartoris fell for a phishing attack recently. It’s hard to say what DEADFACE was after, but Turbo Tactical 
needs your help looking through the attack artifacts. 
Take a look at this memory dump and submit the system time on which the memory was captured.

Submit the flag as flag{YYYY-MM-DD hh:mm:ss+00:00}.

## Solution

https://ctf101.org/forensics/what-is-memory-forensics/

```sh
python2.7 /opt/volatility/vol.py -f ~/coding/repos/ctf/deadface-ctf-2024/misc/phantom-operators/right-time/physmem.raw imageinfo
# INFO    : volatility.debug    : Determining profile based on KDBG search...
#           Suggested Profile(s) : No suggestion (Instantiated with Win10x64_19041)
#                      AS Layer1 : SkipDuplicatesAMD64PagedMemory (Kernel AS)
#                      AS Layer2 : FileAddressSpace (/home/barrett/coding/repos/ctf/deadface-ctf-2024/misc/phantom-operators/right-time/physmem.raw)
#                       PAE type : No PAE
#                            DTB : 0x1aa000L
#              KUSER_SHARED_DATA : 0xfffff78000000000L
#            Image date and time : 2024-10-06 23:38:00 UTC+0000
#      Image local date and time : 2024-10-06 16:38:00 -0700

strings physmem.raw | less
# BOCHS BXPC    
# BXPC
# /rom@genroms/kvmvapic.bin
# /pci@i0cf8/*@12
# NTFS    
# NTFSu
# Microsoft Corporation1.0,
# %Microsoft Windows Production PCA 20110

strings physmem.raw > strings.txt

```

winupdate.exe looks suspicious


flag{YYYY-MM-DD hh:mm:ss+00:00}
2024-10-06 16:38:00 -0700

2024-10-06 23:38:00 UTC+0000
flag{2024-10-06 23:38:00+00:00}
