h = '2b3e49392b624522327235462b614960322768452b614962796164392b3e6437226223403528494035276824796149642b28393735613539327235462a28354429612b403576753f333f5f6c'
ascii_chars = []
    
for i in range(0, len(h), 2):
    p = h[i:i+2]
    i = int(p, 16)
    c = chr(i)
    print(p, '=', i, '=', c)

    ascii_chars.append(c)

print(''.join(ascii_chars))
