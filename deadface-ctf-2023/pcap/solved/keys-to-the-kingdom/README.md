# keys-to-the-kingdom

An image was sent across De Monne Financial’s network. 
They’re still paranoid after being the primary target of DEADFACE last year, and they suspect this is DEADFACE activity. 
We’re not sure what to make of the PCAP they sent us, but we found a file on the anomalous De Monne machine named `keytothekingdom.txt`. 
We suspect that contents of the file have undergone some form of encoding or encryption. 
See if you can piece these two things together to find the flag in the pcap.

Submit the answer as flag{here-is-the-answer}.

Download PCAP File
SHA1: 8c8f8b9d3935067ba1e67baa6d939ea68e881c90

Key ciphertext: `ÓÄÖëÄøõàñããàøâñãõùãªÞåýåøåûåýñûùñûùñùñüåþñýÿâí`

## Solution

`Thekeytothekingdom.pcap`

downloaded hex stream to `payload.txt`, threw into cyberchef from hex.
saved output as jpg

top looks like it says 12:43AM, rest is cutoff

Oh...all the packets have a part of the image

`extract.py`

`Mike wahousekey`

`flag{Mike wahousekey}` nope

I guess this is key to ciphertext?

ciphertext to hex `d3c4d6ebc4f8f5e0f1e3e3e0f8e2f1e3f5f9e3aadee5fde5f8e5fbe5fdf1fbf9f1fbf9f1f9f1fce5fef1fdffe2ed`

```sh
steghide extract -sf payload.jpg -xf extracted -p 'Mike wahousekey'

steghide extract -sf payload.jpg -xf extracted -p 'ÓÄÖëÄøõàñããàøâñãõùãªÞåýåøåûåýñûùñûùñùñüåþñýÿâí'

steghide extract -sf payload.jpg -xf extracted
```

note: there is an http stream in 4 of the packets?

`CTF{Thepassphraseis:Numuhukumakiakiaialunamor}`

uhh what?

- `CTF{Thepassphraseis:Numuhukumakiakiaialunamor}`
- `flag{Thepassphraseis:Numuhukumakiakiaialunamor}`
- `flag{Numuhukumakiakiaialunamor}`

```sh
binwalk payload.jpg
strings payload.jpg
```

Oh

```sh
steghide extract -sf payload.jpg
# passphrase=Numuhukumakiakiaialunamor
```

`flag{Error404FlagNotFound}`
