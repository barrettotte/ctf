# Drink Up

While responding to a recent security incident, TGRI found the following image on an employee’s compromised machine. 
We need to confirm which DEADFACE actor attacked TGRI.

There’s probably one or more hints in the image that will point you in the right direction.

Submit the flag as flag{flag}.

## Solution

Well I was close, guess I was using the wrong site for XXTEA decrypt.

cyberchef: base64 decode, then XXTEA decrypt with key `Tea Turned Up to the Max!`

## Attempt

```sh
strings callingcard.png | less
# adobe photoshop

binwalk -Me callingcard.png

pngcheck -qv callingcard.png
```

```txt
zxk1ehfZ/kx7tzSyQeSm2XuGitnxsN8rG/mwxNaCjFFc2rCrTTWpwViZFpwI4xRccvdwm/Ta6l3GFeaPs96l7BPziIu+DsfoS6bdy5ByHSyW+D5bCgtTCuoVvMOlPC7xILtjlt6/Ky6ZPaV40gfmtM/iuRGR+zveFLNyWy9Tlu3TnOaq0lP6wp65lGEFBTHPSwho0jIP47pxoKryxnh7svJrTD1wh+D+YudNjDpPr39yH/iMlU+5xiK2dXjiD0UtL3vSSQ55MLCPpN/kFW6AuO2OEuadKXg2XYiXnAkLJcUxGdZhP7+Lo4LG3m5HsHdBmul5pX9gcvERFQSZOy2QfEv3+vRfLfoJPq6WQnBjwXUoVo/YHeD8SS+TDvg=
```

beer encryption (multiple methods?)
picture says 2 ingredients?

base 64 and XXTEA encryption?

https://github.com/xxtea/xxtea-python

