# Bad Blood

Nothing is more dangerous than a bad guy that used to be a good guy. Something's going on... please talk with our incident response team.

nc chal.competitivecyber.club 10001 

## Solution

```txt
Q1. Forensics found post exploitation activity present on system, network and security event logs. What post-exploitation script did the attacker run to conduct this activity?
        Example answer: PowerView.ps1
Untitled1.ps1 - nope
Invoke-UrbanBishop.ps1 - nope
C:\Users\jack\Downloads\Invoke-UrbanBishop.ps1 - nope
Invoke-p0wnedShell - nope
Invoke-p0wnedShell.ps1

Q2. Forensics could not find any malicious processes on the system. However, network traffic indicates a callback was still made from his system to a device outside the network. We believe jack used process injection to facilitate this. What script helped him accomplish this?
        Example answer: Inject.ps1
Invoke-UrbanBishop.ps1

Q3. We believe Jack attempted to establish multiple methods of persistence. What windows protocol did Jack attempt to abuse to create persistence?
        Example answer: ProtoName
winrm

Q4. Network evidence suggest Jack established connection to a C2 server. What C2 framework is jack using?
        Example answer: C2Name
BlockEtw - nope
cobaltstrike - nope
cobalt strike - nope
PSRansom - nope
p0wnedShell - nope
UrbanBishop - nope
Covenant - nope
```

https://raw.githubusercontent.com/IAMinZoho/OFFSEC-PowerShell/main/Invoke-P0wnedshell.ps1
first payload base64 decode to `download.gz`, extract to `download`

`strings download | less`

p0wnedShellOpsec

Invoke_Mimikatz
Remote_Mimikatz

https://github.com/IAMinZoho/OFFSEC-PowerShell/blob/main/Invoke-UrbanBishop.ps1

just googled powershell c2 framework - Covenant

`pctf{3v3nt_l0gs_reve4l_al1_a981eb}`
