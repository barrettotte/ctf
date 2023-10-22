
with open('reflections2.txt', 'r') as f:
    src = f.read()
# print(src)

bin_strings = [bin(ord(c))[2:].zfill(8) for c in src]
print(bin_strings)

unique = set(bin_strings)
print(len(unique), 'unique strings')
print(unique)

# https://planetcalc.com/8640/
lookup = {
    # gray       bin
    '01010010': '01100011', # 99
    '01010011': '01100010', # 98
    '01000100': '01111000', # 120
    '00101111': '00110101', # 53
    '01010111': '01100101', # 101
    '01010001': '01100001', # 97
    '00101101': '00110110', # 54
    '00100101': '00111001', # 57
    '01010101': '01100110', # 102
    '00101000': '00110000', # 48
    '00101001': '00110001', # 49
    '00101011': '00110010', # 50
    '00101100': '00110111', # 55
    '01010110': '01100100', # 100
    '00100100': '00111000', # 56
    '00101010': '00110011', # 51
    '00101110': '00110100', # 52
}

decoded = []
for b in bin_strings:
    decoded.append(lookup[b])

with open('decoded.txt', 'w+') as f:
    f.write(''.join(decoded))
