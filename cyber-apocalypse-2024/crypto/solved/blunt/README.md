# blunt

Valuing your life, you evade the other parties as much as you can, forsaking the piles of weaponry and the vantage points in favour of the depths of the jungle. As you jump through the trees and evade the traps lining the forest floor, a glint of metal catches your eye. Cautious, you creep around, careful not to trigger any sensors. Lying there is a knife - damaged and blunt, but a knife nonetheless. You’re not helpless any more.

## Solution

bruteforced original values:

a = 2766777741
b = 1913706799


HTB{y0u_n3ed_a_b1gGeR_w3ap0n!!}

## Post-CTF

https://youtu.be/EGItzKCxTdQ?si=bgwcpgr4sfNlKBCn&t=7422

Diffie-Hellman challenge

use sagemath

```txt
p = 0xdd6cc28d
g = 0x83e21c05
A = 0xcfabb6dd
B = 0xc4a21ba9
R = Integers(p)
g = R(g)
A = R(A)
A.log(g) # 2766777741
```
