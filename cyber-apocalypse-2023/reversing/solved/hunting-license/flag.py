h = '477b7a6177527d77557a7d727f32323213'
pwd_bytes = bytearray.fromhex(h)
pwd_bytes = bytes([b ^ 0x13 for b in pwd_bytes])

print(pwd_bytes)
