import binascii
from Crypto.Cipher import AES

encrypted = b'5f558867993dccc99879f7ca39c5e406972f84a3a9dd5d48972421ff375cb18c'
key = b'supersecretkeyusedforencryption!'
iv = b'someinitialvalue'

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(encrypted)
print(f'{decrypted=}')
print(binascii.unhexlify(decrypted))
