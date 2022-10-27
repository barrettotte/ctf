from Crypto.Cipher import AES

key = 'vN0nb7ZshjAWiCzv'
iv = b'ffTC776Wt59Qawe1'

cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv)

with open('/home/barrett/Downloads/candy_dungeon.pdf.boo', 'rb') as f_in:
    encrypted = f_in.read()

    with open('/home/barrett/Downloads/candy_dungeon.pdf', 'wb') as f_out:
       decrypted = cipher.decrypt(encrypted)
       f_out.write(decrypted)
