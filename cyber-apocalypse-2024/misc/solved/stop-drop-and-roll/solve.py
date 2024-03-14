from pwn import *

io = remote('94.237.53.26', 31490)

io.recvuntil(b'(y/n)')
io.sendline(b'y')

cmd_map = {
    'GORGE': 'STOP',
    'PHREAK': 'DROP',
    'FIRE': 'ROLL'
}

prompt = b'What do you do?'

print(io.recvuntil(b"Ok then! Let's go!\n"))

i = 0
while True:
    try:
        line = io.recvuntil(prompt)
        cmds = line.decode().split('\n')[0].split(',')
        cmds = [cmd.strip() for cmd in cmds]
    except Exception as e:
        print(e)
        break

    resp = '-'.join([cmd_map[cmd] for cmd in cmds])
    print(i, '-', cmds, '->', resp)
    io.sendline(resp.encode())
    i += 1

print(io.recv(128))
