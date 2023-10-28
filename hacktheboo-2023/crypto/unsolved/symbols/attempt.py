from random import randint
from Crypto.Util import number
import binascii

p = 307163712384204009961137975465657319439
g = 1337

def encrypt(m):
    bits = bin(m)[2:] # removes '0b'
    print('bits:', len(bits))

    encrypted = []
    for b in bits: # 279
        r = (randint(2, p) << 1) + int(b)
        encrypted.append(pow(g, r, p))
    return encrypted

##########################################################################################

def decrypt(encrypted):
    decrypted = []
    for i in encrypted:
        # r = (randint(2, p) << 1) + int(b)
        # encrypted.append(pow(g, r, p)) # i = g^r (mod p)
        
        # r = log_g(i) (mod p) --- discrete logarithm

        r = number.inverse(g, p) * i % p
        # r = number.inverse(i, p) * g % p

        b = r & 1
        decrypted.append(b)
    return decrypted

with open('output.txt', 'r') as f:
    encrypted = f.read().replace('[',',').replace(']',',').split(',')
    encrypted = [int(e) for e in encrypted[1:-1]]
print('encrypted nums:', len(encrypted))

decrypted = decrypt(encrypted)
print(len(decrypted), 'decrypted bits')
decrypted = ''.join([str(i) for i in decrypted])
print(decrypted)

decrypted = int(decrypted, 2)
decrypted = number.long_to_bytes(decrypted)
decrypted = binascii.hexlify(decrypted)
print(decrypted)
