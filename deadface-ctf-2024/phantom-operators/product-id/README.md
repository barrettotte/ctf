# Product ID

We suspect that Garry Sartoris was using a non-compliant Windows host and not his work-provided laptop from TGRI. Is there any way to confirm this in the data that DEADFACE exfiltrated? Provide the Windows Product ID of Garry Sartoris’s machine.

Submit the flag as flag{Windows Product ID}. Example: flag{12345-67890-12345-67890}.

## Solution

Use PCAP from big-fish

```txt
0000   02 6b 2c 8f 50 4e 94 10 3e 95 47 ea 08 00 45 00   .k,.PN..>.G...E.
0010   02 40 36 41 00 00 2e 01 89 e3 2d 37 c9 bc 0a 41   .@6A......-7...A
0020   c9 64 03 03 7f 96 00 00 00 00 45 00 04 1c 6a 9e   .d........E...j.
0030   00 00 6f 11 12 9a 0a 41 c9 64 2d 37 c9 bc cd de   ..o....A.d-7....
0040   11 d7 04 08 a2 25 0d 0a 0d 0a 57 69 6e 64 6f 77   .....%....Window
0050   73 42 75 69 6c 64 4c 61 62 45 78 20 20 20 20 20   sBuildLabEx     
0060   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
0070   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
0080   20 20 3a 20 31 39 30 34 31 2e 31 2e 61 6d 64 36     : 19041.1.amd6
0090   34 66 72 65 2e 76 62 5f 72 65 6c 65 61 73 65 2e   4fre.vb_release.
00a0   31 39 31 32 30 36 2d 31 34 30 36 0d 0a 57 69 6e   191206-1406..Win
00b0   64 6f 77 73 43 75 72 72 65 6e 74 56 65 72 73 69   dowsCurrentVersi
00c0   6f 6e 20 20 20 20 20 20 20 20 20 20 20 20 20 20   on              
00d0   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
00e0   20 20 20 20 20 3a 20 36 2e 33 0d 0a 57 69 6e 64        : 6.3..Wind
00f0   6f 77 73 45 64 69 74 69 6f 6e 49 64 20 20 20 20   owsEditionId    
0100   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
0110   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
0120   20 20 20 20 3a 20 43 6f 72 65 0d 0a 57 69 6e 64       : Core..Wind
0130   6f 77 73 49 6e 73 74 61 6c 6c 61 74 69 6f 6e 54   owsInstallationT
0140   79 70 65 20 20 20 20 20 20 20 20 20 20 20 20 20   ype             
0150   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
0160   20 20 20 20 3a 20 43 6c 69 65 6e 74 0d 0a 57 69       : Client..Wi
0170   6e 64 6f 77 73 49 6e 73 74 61 6c 6c 44 61 74 65   ndowsInstallDate
0180   46 72 6f 6d 52 65 67 69 73 74 72 79 20 20 20 20   FromRegistry    
0190   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
01a0   20 20 20 20 20 20 3a 20 36 2f 33 30 2f 32 30 32         : 6/30/202
01b0   34 20 37 3a 30 35 3a 31 30 20 50 4d 0d 0a 57 69   4 7:05:10 PM..Wi
01c0   6e 64 6f 77 73 50 72 6f 64 75 63 74 49 64 20 20   ndowsProductId  
01d0   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
01e0   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
01f0   20 20 20 20 20 20 3a 20 30 30 33 32 36 2d 31 30         : 00326-10
0200   30 30 30 2d 30 30 30 30 30 2d 41 41 39 37 33 0d   000-00000-AA973.
0210   0a 57 69 6e 64 6f 77 73 50 72 6f 64 75 63 74 4e   .WindowsProductN
0220   61 6d 65 20 20 20 20 20 20 20 20 20 20 20 20 20   ame             
0230   20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20                   
0240   20 20 20 20 20 20 20 20 20 3a 20 57 69 6e                  : Win

```

`flag{00326-10000-00000-AA973}`
