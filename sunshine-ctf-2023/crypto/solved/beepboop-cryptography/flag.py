
with open('BeepBoop', 'r') as f:
    raw = f.readlines()[0]

msg = raw.split(' ')
msg = ['1' if c == 'boop' else '0' for c in msg]
msg = ''.join(msg)

# convert bin string to ascii
flag = ''
for i in range(0, len(msg), 8):
    flag += chr(int(msg[i:i + 8], 2))

print(flag)
# fha{rkgrezvangr-rkgrezvangr-rkgrezvangr|

# https://www.dcode.fr/cipher-identifier
# https://www.dcode.fr/affine-cipher

# sun{exterminate-exterminate-exterminate|
# sun{exterminate-exterminate-exterminate}
