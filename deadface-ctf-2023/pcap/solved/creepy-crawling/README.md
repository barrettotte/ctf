# creepy-crawling

One of our clients, TGRI, had an SSH server compromised at one of their smaller remote locations. 
Their only security analyst was fired and “accidentally” deleted information specific to the attack. 
Thankfully, TGRI still has the PCAP that captured the SSH brute force attack. 
What SSH protocol did TGRI run that was eventually compromised by DEADFACE?

Submit the SSH protocol as the flag: flag{SSH-1.1.1: Simple SSH Server}

## Solution

wireshark

ssh - tcp 22

filter: ssh

SSH-2.0-9.29 FlowSsh: Bitvise SSH Server (WinSSHD) 9.29

`flag{SSH-2.0-9.29 FlowSsh}`

`flag{SSH-2.0-9.29 FlowSsh: Bitvise SSH Server}`