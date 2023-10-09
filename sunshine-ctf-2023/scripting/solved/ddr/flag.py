from pwn import *

io = remote('chal.2023.sunshinectf.games', 23200)

prompt = b'-- Press ENTER To Start --'
print(io.recvuntil(prompt))
io.recvline(1)

io.sendline() # press enter
io.recvline(1)

arrow_to_key = {
    '⇧': b'W',
    '⇩': b'S',
    '⇨': b'D',
    '⇦': b'A'
}

i = 1
while i < 256:
    # ex: ⇦⇩⇧⇧⇦⇦⇨⇨⇦⇦⇨⇩⇨⇩⇨⇦⇦⇧⇩⇧⇩⇦⇩⇩⇧⇧⇧⇨⇧⇦⇧⇦⇩⇧⇨⇩⇩⇧⇦⇩⇦⇧⇦⇧⇩⇦⇧⇦⇧⇩   (50 characters)
    pattern = io.recv(50 * 3) # unicode = 3 bytes
    pattern = pattern.decode()
    print(str(i) + ':', pattern)

    presses = b''.join([arrow_to_key[c] for c in pattern])
    io.sendline(presses)
    io.recvline()
    io.recv(1)

    i += 1

print(io.recvall())

# sun{d0_r0b0t5_kn0w_h0w_t0_d4nc3}
