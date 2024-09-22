import base64

srt_key = 'secretkey'
c = base64.b64decode(b'QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I=').decode()

p1 = ''
p2 = ''
for i in range(len(c) // 2):
    x = ord(srt_key[i % len(srt_key)])
    p1 += chr(ord(c[i * 2]) ^ x)
    p2 += chr(ord(c[i * 2 + 1]) ^ x)

flag = p1 + p2[::-1]
print(flag)
# 234c81cf3cd2a50d91d5cc1a1429855f
