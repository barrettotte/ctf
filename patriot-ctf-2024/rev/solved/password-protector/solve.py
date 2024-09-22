import os
import secrets
from base64 import *

flipFlops = lambda x: chr(ord(x) + 1)
flipFlopsRev = lambda x: chr(ord(x) - 1)

def encrypt():
    with open('topsneaky.txt', 'rb') as f:
        first = f.read()
    bittys = secrets.token_bytes(len(first))
    onePointFive = int.from_bytes(first) ^ int.from_bytes(bittys)
    second = onePointFive.to_bytes(len(first))
    third = b64encode(second).decode('utf-8')
    bittysEnc = b64encode(bittys).decode('utf-8')
    fourth = ''
    for each in third:
        fourth += flipFlops(each)
    fifth = f"Mwahahaha you will n{fourth[0:10]}ever crack into my pass{fourth[10:]}word, i'll even give you the key and the executable:::: {bittysEnc}"
    return fifth

# fourth    -> Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp
# bittysEnc -> Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV

def decrypt(fourth, bittys_enc):
    reverse_flipFlops = lambda x: chr(ord(x) - 1)
    third = ''.join(reverse_flipFlops(c) for c in fourth)
    
    second = b64decode(third.encode('utf-8'))
    bittys = b64decode(bittys_enc.encode('utf-8'))
    
    onePointFive = int.from_bytes(second, 'big') ^ int.from_bytes(bittys, 'big')
    original = onePointFive.to_bytes(len(second), 'big')
    
    return original


decrypted = decrypt('Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp', 'Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV')
print(decrypted.decode('utf-8'))

# PCTF{I_<3_$3CUR1TY_THR0UGH_0B5CUR1TY!!}
