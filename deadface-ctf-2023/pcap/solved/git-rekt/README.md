# git-rekt

One of our teammates at Turbo Tactical ran a phishing campaign on spookyboi and thinks spookyboi may have submitted credentials. 
We need you to take a look at the PCAP and see if you can find the credentials.

Submit the password as the flag: flag{password}.

## Solution

wireshark

Form item: "login" = "spookyboi@deadface.io"
Form item: "password" = "SpectralSecrets#2023"

`flag{SpectralSecrets#2023}`
