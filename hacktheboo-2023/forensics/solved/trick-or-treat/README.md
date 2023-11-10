# trick-or-treat

Another night staying alone at home during Halloween. 
But someone wanted to play a Halloween game with me. 
They emailed me the subject "Trick or Treat" and an attachment. 
When I opened the file, a black screen appeared for a second on my screen. 
It wasn't so scary; maybe the season is not so spooky after all.

## Solution

some sort of powershell payload in `trick_or_treat.lnk`

opened pcap wireshark

QUIC protocol? https://en.wikipedia.org/wiki/QUIC

```txt
tcp stream 69

GET /filestreamingservice/files/0ee18f6d-5bb2-4a69-abd7-6fb33b65fe1f?P1=1698307181&P2=404&P3=2&P4=f3smAyr2W56dpgl%2fflvXh0li6EnWja438RyARQp0OHVNcV8G5TlxyzWoPISbHdAJCDdLDdXDhFat9I0HgmRLJA%3d%3d

/filestreamingservice/files/0ee18f6d-5bb2-4a69-abd7-6fb33b65fe1f
?P1=1698307181
&P2=404
&P3=2
&P4=f3smAyr2W56dpgl/flvXh0li6EnWja438RyARQp0OHVNcV8G5TlxyzWoPISbHdAJCDdLDdXDhFat9I0HgmRLJA==

```

lnk file cyberchef remove null bytes -> `trick_or_treat.txt`

tcp stream 69 - checking for magic bytes

0a 0d 0a 43 72 32 34 03  00 00 00 74 04 00 00 12

43 72 32 34 -> google chrome extension or packaged app...interesting

extracted HTTP object from packaet 19628

19628 hex cyberchef from hex
 - XOR 1D on fragment `{hs~itrs=Yorm_re0Hmqr|y=f` -> `function DropBox-Upload {`

saved to payload.txt

`HTB{s4y_Pumpk1111111n!!!}`
