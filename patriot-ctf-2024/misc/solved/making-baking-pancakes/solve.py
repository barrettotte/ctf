import base64
from pwn import *

io = remote('chal.pctf.competitivecyber.club', 9001)

challenge_iter = 0

while challenge_iter < 1000:
    s = io.recvuntil(b'>>').decode('utf-8')
    challenge = s.split('Challenge: ')[1].split('\n')[0]
    challenge = base64.b64decode(challenge.encode('utf-8'))
    challenge = challenge.decode('utf-8').split('|')

    decoded = challenge[0]
    count = int(challenge[1])

    i = 0
    while i < count:
        # print(i, '=', decoded)
        decoded = base64.b64decode(decoded).decode('utf-8')
        i += 1
    # print(decoded)

    solution = (decoded + '|' + str(challenge_iter)).encode('utf-8')
    print(solution)
    io.sendline(solution)
    challenge_iter += 1

print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())

# pctf{store_bought_pancake_batter_fa82370}
