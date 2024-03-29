# i just simulate the encryption again to get the expression and use Z3 solver

from bitstring import BitArray
# from sage.all import *
from z3 import *
import os
from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Util.number import bytes_to_long as btl
def xor(a, b):
    return bytes([i^j for i, j in zip(a, b)])

IV = "01011010000111001011101010000011001000001111001110010111010001011000101011111111"
enc = b'\n_\x02s\xe6\xb4\xf5\xec\xfe\xd6\xb0\xb6\xfb\xf1\x9ab\xb7\x85p(p\x8e\xaf/\xa4\'\xbf\x00\xf4\xac}c\x1e\x83\x00\xee\xcb\x90\x10\n\x91K,\xa3C`\x12w\xe8\x93\x0e+N\xba\xfa\xf9\xf7\xaf\x8f\t\xc3\xa0\xdf\x11\x07K\xb6\x17\xa0\xe3\xbdod\x0e\xbd\xc0\xf8\x90\xa2\xb5\xef\xdf\xa6\x9f\x04xW\x94\xc4\x97\xde,\xda\xb64\xf7\xde\xbeF8W\xfe\xa2\xcc\xf1\xe1O!\xe6#\xeb\x9d\xa9JT\x7f\xbd\xde\xf8\xd1\xec\x0b\x8f-\xf3q_y\xe4\xf7O\xfc\x86\xfa\xb9\xa5\x1d\x10\xc6\xde\xbb\xcc\xe5/\x81\xd4OO"i~\x95\xf5|V\x08sJcB\x88\x1c;p\xec|!\xdb\xd0\x98lg\x0c\xe9=\xf5\xf0\xd3\tz\xab\xb4\xa7\\V\xe6\t\x92\x88\x00\xe9TC\xf6.\xc7q7+.\x92\x0c\x83\x9a.N\x84}\xe9\x0eiU\x10\xc0\x82E\x8b\xefl\xdb\x01\x03\xea\xe2)}\xe0\x07\x02h\xfc\xa0\xdc\x7f\xfb\xa9[\x19\xdc\xa1\xfb\xc4Yv\x1cm\xa0\x8dY\xd6\x16f\x14\\\xf0\xb1\xd3n\x82S[\xeb\xa0sz"\x05\xea\xe2\x0f\xd0n\x0c\xfc\xaf\xee\xe7+c\xa2~K\\\x8f\xd3\xeb%\x87\xb2f.\xa9\x1b\xe9\x07\x1aP\x81&\xf0\xc1\x9aw\xf3\xcb\x93,\x1b\xdf\xfc\xaf\xb3?Q.S\xec\xc8g!tY\x99\xe8\x98\x14\x8c\x89\xdf\xbbv\xdf\x82\xd6\xb4tn\xec\xd1\xb1`@2kA*\x0b\xb9?A\xce\xd03\xb3\xf2\xbbV/\t\'\xdf5\x81\xc5\x15\x8eB]E\xdd\xd6R\xf6\x9c8\xe5\x84\x15\x11\x1a_\x84\xb7\x9e\xec\xbd\x1ed\x17{J\xb8*\xe1\x82\xd4l\xd3\x8bod?\x0b\x1a\xe5t\x18\xbbh5yK\xbeR+\xa7G\x16\xc1\xa7p\xaf\x9c\x9e|\xce^\xf7%\xe4\xd0\xc2\x87\xac\x14\xb4\xa3\xbb\xf7\xb3&\xccaaY\xd0\xb3\xe3\xc7\xfb\xa8\x96ir5c\xf1[j\xdc\xe5\'\x9a\xc5~{\xb5)\xcb\xab\xbe\xa9\x12X\x82\x088\xbf\x8c\x9caX\x8cxw\xbeMu#\xfe:\xcf\x1f\xc9\xbe\x11\t2\xe4\x97\x94<T\xc4\xa7\xf3\x8c\xdf\x9a\x0bHkx\xcc#\xf2\xf0{\x10\xf728}\xd7\x8e\x90\x9ce\xde\x19O?\xbb\x94IH\xd4vj\xd1C\x9f\x18\xf7\xf6=\x92p_\x82\x06\xf8\xe7\xdb\x15\x84|~hP\x88\n\xc7d\xc4\x8f\x08Z^>\xea\xe4\x1c\xd9_\x99\x99\xfc\xa4\xf8\x00\x01\xf0\xf1\x1e\xf5\x1f\xe4\x84\x0b`&/\xcd\xd2\xb7-?\xca'
pt = '''There once was a ship that put to sea
The name of the ship was the Billy O' Tea
The winds blew up, her bow dipped down
Oh blow, my bully boys, blow (huh)

Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go

She'd not been two weeks from shore
When down on her right a whale bore
The captain called all hands and swore
He'd take that whale in tow (huh)

Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go

- '''.encode('utf-8')


def str2bool(x): return bool(int(x))

suffix = list(map(str2bool, '0101000001010' + IV + '0'*4))
stream = list(map(str2bool, f"{btl(xor(pt, enc)):0{len(pt)*8}b}"))
# # B = BooleanPolynomialRing(80, [f'x{i}' for i in range(80)])
# state = list(B.gens()) + suffix

ks = [Bool(f'x{i}') for i in range(80)]
state = ks + suffix

def step():
    global state
    out = Xor(state[65], state[92])
    t1 = Xor(Xor(Xor(state[65], state[92]), And(state[90], state[91])), state[170])
    t2 = Xor(Xor(Xor(state[161], state[176]), And(state[174], state[175])), state[68])
    for i in range(92, 0, -1):
        state[i] = state[i - 1]
    state[0] = t2
    for i in range(176, 93, -1):
        state[i] = state[i - 1]
    state[93] = t1
    return out

print(state)
for _ in range(708):
    step()
print("done")
# print(state[0])
set_option("parallel.enable", True)
set_option("parallel.threads.max", os.cpu_count())
s = Solver()
for i in range(200):
    s.add(step() == stream[i])
if s.check() == sat:
    print("Sat")
    m = s.model()
    key = []
    for i in ks:
        key.append(int(eval(str(m[i]))))
    print(key)
else:
    print("Nope")