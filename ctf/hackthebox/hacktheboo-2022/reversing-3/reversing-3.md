# Reversing 3 - Ghost Wrangler

```sh
file ghost
# ELF 64 pie, dynamically linked

ltrace ./ghost
# HTB{h4unt3d_by_th3_gh0st5_0f_ctf"
# 'HTB{h4unt3d_by_th3_gh0st5_0f_ctf5_p
#

strings ghost
# [GQh{'f}g wLqjLg{ Lt{#`g&L#uLpgu&Lc'&g2n%s

# only promising looking string
# used https://gchq.github.io/CyberChef/#recipe=Magic(5,true,false,'HTB%7B')&input=W0dRaHsnZn1nIHdMcWpMZ3sgTHR7I2BnJkwjdUxwZ3UmTGMnJmcybiVz

_
```
