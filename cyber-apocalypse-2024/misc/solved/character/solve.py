

# Which character (index) of the flag do you want? Enter an index: 

from pwn import *

io = remote('94.237.55.246', 30816)

prompt = b':'

flag = []
i = 0
while i < 200:
    io.recvuntil(prompt)
    io.sendline(f'{i}'.encode())
    try:
        x = io.recvline().decode().split(':')[1].rstrip('\n').lstrip()
    except Exception as e: 
        break
    print(i, '=', x)
    flag.append(x)
    i += 1
    

print(''.join(flag))

# HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}
