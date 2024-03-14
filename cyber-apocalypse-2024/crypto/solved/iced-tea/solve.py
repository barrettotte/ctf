from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import unpad

BLOCK_SIZE = 64
DELTA = 0x9e3779b9

k = bytes.fromhex('850c1413787c389e0b34437a6828a1b2')
KEY = [bytes_to_long(k[i:i+BLOCK_SIZE//16]) for i in range(0, len(k), BLOCK_SIZE//16)]


def decrypt(ct):
    blocks = [ct[i:i+BLOCK_SIZE//8] for i in range(0, len(ct), BLOCK_SIZE//8)]
        
    pt = b''
    for block in blocks:
        pt += decrypt_block(block)
    # return unpad(pt, BLOCK_SIZE)
    return pt


def decrypt_block(msg):
    m = bytes_to_long(msg)
    m0 = m >> (BLOCK_SIZE // 2)
    m1 = m & ((1 << (BLOCK_SIZE // 2)) - 1)
    K = KEY
    msk = (1 << (BLOCK_SIZE // 2)) - 1

    s = DELTA << 5
    for i in range(32):
        m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
        m1 &= msk
        m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
        m0 &= msk
        s -= DELTA

    return long_to_bytes((m0 << (BLOCK_SIZE // 2)) + m1)

ciphertext = bytes.fromhex('b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843')
decrypted = decrypt(ciphertext)

print(decrypted)
# HTB{th1s_1s_th3_t1ny_3ncryp710n_4lg0r1thm_____y0u_m1ght_h4v3_4lr34dy_s7umbl3d_up0n_1t_1f_y0u_d0_r3v3rs1ng}
