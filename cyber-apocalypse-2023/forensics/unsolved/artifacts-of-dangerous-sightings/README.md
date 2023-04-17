# artifacts-of-dangerous-sightings

> Pandora has been using her computer to uncover the secrets of the elusive relic. 
> She has been relentlessly scouring through all the reports of its sightings. 
> However, upon returning from a quick coffee break, her heart races as she notices the Windows Event Viewer tab open on the Security log. 
> This is so strange! 
> Immediately taking control of the situation she pulls out the network cable, takes a snapshot of her machine and shuts it down. 
> She is determined to uncover who could be trying to sabotage her research, and the only way to do that is by diving deep down and following all traces ...

TODO: review writeup

HackTheBox discord

```txt
The file is hidden in something called alternate data streams (a single file may contain multiple files, sort of, the filename:stream1 is the format, https://www.malwarebytes.com/blog/news/2015/07/introduction-to-alternate-data-streams).

Here's how I did it after several unsuccessful tries (using guestmount and  getfattr on the file to extract the xattr didn't work):

1. sudo qemu-nbd -c /dev/nbd0 2023-03-09T132449_PANDORA.vhdx
2. sudo mount -o ro,loop,show_sys_files,streams_interface=windows /dev/nbd0p1 evidence/
3. cat ActiveSyncProvider.dll:hidden.ps1
```

## Attempt

vhdx file? oh, hyper-v disk

```ini
# E:\C\Users\Pandora\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar
[LocalizedFileNames]
File Explorer.lnk=@%SystemRoot%\system32\shell32.dll,-22067
```

```txt
# E:\C\Users\Pandora\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline

type finpayload > C:\Windows\Tasks\ActiveSyncProvider.dll:hidden.ps1
exit
Get-WinEvent
Get-EventLog -List
wevtutil.exe cl "Windows PowerShell" 
wevtutil.exe cl Microsoft-Windows-PowerShell/Operational
Remove-EventLog -LogName "Windows PowerShell"
Remove-EventLog -LogName Microsoft-Windows-PowerShell/Operational
Remove-EventLog 
```

E:\C\ProgramData\Microsoft\search\data\applications\windows\GatherLogs\SystemIndex
.crwl and .gthr files

sqllite db at c/users/pandora/appdata/local...

mmc.exe

```
CMD
{"gdprType":"ProductAndServiceUsage","clipboardDataId":"{8BA4CF1A-D2A1-4F16-B5E4-5755900E0EF4}"}
```

```json
[{"application":"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\notepad.exe","platform":"windows_win32"},{"application":"{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}\\notepad.exe","platform":"windows_win32"},{"application":"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\notepad.exe","platform":"packageId"},{"application":"","platform":"alternateId"}]

{"displayText":"Relic Archives.txt","activationUri":"ms-shellactivity:","appDisplayName":"Notepad","description":"C:\\Users\\Pandora\\Desktop\\Relic Archives.txt","backgroundColor":"black","contentUri":"file:///C:/Users/Pandora/Desktop/Relic%20Archives.txt?VolumeId={C68F7155-6FD3-40A9-B141-55132BC1EA43}&ObjectId={0967B823-BE6B-11ED-9C97-3CE9F7AFEF2D}&KnownFolderId=ThisPCDesktopFolder&KnownFolderLength=24"}
```

https://www.autopsy.com/download/

```powershell
Convert-VHD -Path c:\Downloads\2023-03-09T132449_PANDORA.vhdx -DestinationPath c:\Downloads\2023-03-09T132449_PANDORA.vhd

# Windows feature needs to be enabled
# Hyper-V | Hyper-V Management tools | Hyper-V Module for Windows PowerShell
# didnt work
```

```sh
apt install qemu-utils
qemu-img convert -p -f vhdx -O vmdk /mnt/c/Users/Barrett/Downloads/2023-03-09T132449_PANDORA.vhdx /mnt/c/Users/Barrett/Downloads/2023-03-09T132449_PANDORA.vmdk
# worked!
```

opened new vmdk in autopsy
