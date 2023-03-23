from pwn import *

def calculate(eq):
    try:
        solution = round(eval(eq), 2)
        # print(solution)
        if solution < -1337.00 or solution > 1337.00:
            return 'MEM_ERR'
        else:
            return f'{solution:.2f}' if isinstance(solution, float) else str(solution)
    except ZeroDivisionError:
        return 'DIV0_ERR'
    except SyntaxError:
        return 'SYNTAX_ERR'

io = remote('159.65.62.241',32586)

print(io.recvuntil(b'>'))
io.sendline(b'1')

for i in range(0,501):
    try:
        io.recvuntil(b':', timeout=200)
        eq = io.recv(timeout=200).decode().split('=')[0]
    except EOFError as e:
        try:
            print(io.recvline(20))
            print(e)
        except EOFError:
            pass
        finally:
            exit(1)
    
    print(f'[{i}]: ', eq, end=' ')

    solution = calculate(eq)

    print('=', solution)
    io.sendline(str.encode(solution))

try:
    io.recvline(20)
except EOFError:
    pass

io.interactive()