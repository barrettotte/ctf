# alien-cradle

**SOLVED**

> In an attempt for the aliens to find more information about the relic, they launched an attack targeting Pandora's close friends and partners that may know any secret information about it. 
> During a recent incident believed to be operated by them, Pandora located a weird PowerShell script from the event logs, otherwise called PowerShell cradle. 
> These scripts are usually used to download and execute the next stage of the attack. 
> However, it seems obfuscated, and Pandora cannot understand it. 
> Can you help her deobfuscate it?

just read powershell script `cradle.ps1`, flag plaintext

```ps1
$f = 'H' + 'T' + 'B' + '{p0w3rs' + 'h3ll' + '_Cr4d' + 'l3s_c4n_g3t' + '_th' + '3_j0b_d' + '0n3}';
```

`HTB{p0w3rsh3ll_Cr4dl3s_c4n_g3t_th3_j0b_d0n3}`
