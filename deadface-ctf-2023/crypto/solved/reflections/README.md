# reflections

Apparently one of the DEADFACE members disclosed their public key in some fashion on GhostTown. 
We tried to decipher the contents but we can’t seem to figure it out. 
If you can figure out how to decode this public key, it might come in handy later!

Submit the flag as flag{flag text}.

## Solution


https://ghosttown.deadface.io/t/pubs-from-everyone/97/8

```
It uses some sequence from Bell Labs in the 1940s. 
I just learned about it in my comp sci class and thought I’d try it out. 
I think it’s called like reflected binary or something like that.
```

```
(D+V(D+V(D+V(D+V(D+V(D.+(D./(D.,(D.%(D.W(D+((D/((D//(D.+(D.R(D.%(D.*(D+((D.S(D./(D/%(D+V(D+V(D+V(D+V(D+V(D(V(D(Q(D.V(D.%(D.,(D--(D.V(D.)(D*((D.,(D.*(D/*(D,)(D.,(D/*(D.%(D-+(D**(D..(D/)(D./(D.+(D.)(D/)(D//(D.)(D.)(D*.(D.,(D.W(D.)(D..(D.*(D.+(D-%(D/)(D.S(D.+(D-,(D/)(D.*(D*-(D.+(D/*(D*%(D/$(D.,(D-Q(D/-(D/((D,Q(D-/(D-S(D-*(D-U(D-,(D*+(D,+(D.Q(D*.(D-S(D.*(D-V(D-Q(D.,(D,$(D(V(D(Q(D*/(D.-(D.+(D+U(D.$(D-U(D-/(D-U(D*)(D,((D-S(D.$(D*)(D**(D.%(D.%(D.-(D/Q(D-R(D-Q(D.$(D*%(D.U(D..(D.*(D,.(D,-(D.V(D,,(D/((D//(D**(D-V(D//(D.%(D*.(D.U(D.U(D-/(D*,(D/*(D,%(D-.(D*((D-V(D,%(D.S(D-/(D/$(D.R(D-*(D+S(D-V(D,)(D*+(D.%(D,.(D-/(D,)(D-.(D..(D-,(D-)(D/+(D(V(D(Q(D*)(D*.(D,/(D.$(D,*(D.,(D/%(D-R(D.W(D-+(D-)(D-U(D.)(D*,(D,+(D.-(D+S(D/((D--(D-*(D,,(D/-(D.+(D,((D,%(D-/(D*+(D/.(D+U(D.%(D-+(D.%(D/Q(D/,(D-W(D/Q(D*/(D*.(D/-(D/%(D-/(D.+(D.-(D.*(D*((D.U(D/%(D*/(D/$(D-.(D/+(D/,(D/.(D,Q(D+U(D,)(D*,(D.S(D-,(D.*(D.S(D,)(D,-(D*$(D(V(D(Q(D-R(D*.(D-U(D,/(D-)(D.W(D..(D/.(D..(D,%(D-.(D-$(D.S(D.V(D+U(D/)(D//(D/)(D.%(D..(D.)(D/)(D.)(D.+(D(V(D(Q(D+V(D+V(D+V(D+V(D+V(D./(D.W(D..(D+((D/((D//(D.+(D.R(D.%(D.*(D+((D.S(D./(D/%(D+V(D+V(D+V(D+V(D+V(D(Q(D(Q(D--(D-R(D-)(D-,(D,S(D*+(D--(D*)(D-*(D**(D-.(D*)(D-.(D-)(D-*(D**(D-*(D*.(D--(D*/(D-+(D*+(D-+(D**(D*$(D*/(D*-(D*,(D*.(D*/(D*%(D-.(D*-(D-*(D*.(D**(D*((D,V
```

- https://en.wikipedia.org/wiki/Gray_code
- https://www.dcode.fr/gray-code
- https://www.youtube.com/watch?v=cbmh1DPPQyI
- https://planetcalc.com/8640/

`decode.py`

put contents of `decoded.txt` into cyberchef
from binary -> from hex

```txt
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6BS9XGjVPzekcog2rJ4kCmjGx
5FB/Hoeo1pkH13IIFZljH9ODCtvMwPU3mUI4OOe7Syd0myKeXLc+mq2IteqdDgaR
14uHsGYlNbaoA7rF+PfcwVBpye2T/IbIZWnZ54VYeBFC0OY5XdRWTz/q7KgCKqv8
l4ouaNDTDydhKM/QUQIDAQAB
-----END PUBLIC KEY-----

flag{2f1c3d1dac3c4f5b2b38567459d6c430}
```

`flag{2f1c3d1dac3c4f5b2b38567459d6c430}`

note: maybe public key needed later?
