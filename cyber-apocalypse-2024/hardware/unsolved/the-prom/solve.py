from pwn import *

io = remote('94.237.62.48', 38774)

prompt = b'>'
print(io.recvuntil(prompt))
print(io.recvuntil(prompt))
# io.recvline(1)

i = 0
# a0-a10 = 11-bit, 2^11 = 2048 words

io.sendline(b'set_ce_pin(5)')
io.recv(1)
io.sendline(b'set_oe_pin(5)')
io.recv(1)
io.sendline(b'set_we_pin(0)')
io.recv(1)

data = []
while i < 2048:
    addr = [5 if x=='1' else 0 for x in list(format(i, '011b'))]
    print('addr', i, '=', addr)
    cmd = f'set_address_pins({str(addr)})'
    # print(cmd)
    io.sendline(cmd.encode())
    io.recv(1)

    cmd = 'read_byte()'
    io.sendline(cmd.encode())

    b = io.recvline().decode().split(' ')
    idx = b.index('at')-1
    # print(b)
    print('byte read:', b[idx])
    data.append(b[idx])

    io.recvuntil(prompt)

    i += 1

print(data)
with open('data.txt', 'w+') as f:
    f.write('\n'.join([str(s) for s in data]))

# set_address_pins([1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1])
# set_ce_pin(5)
# set_oe_pin(5)
# set_we_pin(0)
# read_byte()

# 0x7E0  set_address_pins([5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0])
# 0x7FF  set_address_pins([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
