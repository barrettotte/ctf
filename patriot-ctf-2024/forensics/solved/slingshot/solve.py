
def decrypt(encrypted, enc_time):
    key = str(enc_time).encode('utf-8')
    key_len = len(key)
    data_len = len(encrypted)
    temp1 = data_len // key_len
    temp2 = data_len % key_len
    key *= temp1
    key += key[:temp2]

    return bytes((a ^ b for a, b in zip(key, encrypted)))

# try to figure out correct epoch time to use
# enc_epoch = 1726895588
enc_epoch = 1726595769

with open('encrypted.bin', 'rb') as r:
    encrypted = r.read()

for i in range(0, 1, 1):
    t = enc_epoch + i
    decrypted = decrypt(encrypted, t)
    with open(f'decrypt/decrypted-{t}.bin', 'wb') as f:
        f.write(decrypted)
