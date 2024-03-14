encrypted = '!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB'


decrypted = ''
for i in range(2, len(encrypted), 3):
    decrypted += encrypted[i]
    decrypted += encrypted[i-2]
    decrypted += encrypted[i-1]

print(decrypted)

# }!?!Dede3n_5i_nOpa3w_ReTt3b_4{BTH
# HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}
