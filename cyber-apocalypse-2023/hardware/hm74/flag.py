

# def decode(m):
#     a, b, c, d = (m[0], m[1], m[2], m[3])
#     return d + c + b + a

# def encode(m):
#     a, b, c, d = (m[0], m[1], m[2], m[3])
#     p0 = d ^ c ^ a
#     p1 = d ^ b ^ a
#     p2 = c ^ b ^ a

#     ham_out = p0 + p1 + d + p2 + c + b + a
#     if len(ham_out) != 8:
#         raise Exception('bad length')
#     return ham_out

def calc_redundant_bits(m):
    # 2 ^ r >= m + r + 1
    for i in range(m):
        if(2**i >= m+i+1):
            return i
        
def pos_redundant_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''

    for i in range(1, m+r+1):
        if i == 2**j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1*k]
            k += 1
    return res[::-1]

def calc_parity_bits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n+1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1*j])
    arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detect_error(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n+1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1*j])
        res = res + val*(10**i)
    return int(str(res), 2)

##########################################################

# data = '1011001'
# m = len(data)
# r = calc_redundant_bits(m)
# arr = pos_redundant_bits(data, r)
# arr = calc_parity_bits(arr, r)
# print('data transferred:', arr)

# arr = '11101001110'
# print('data received is:', arr)
# correction = detect_error(arr, r)
# if correction == 0:
#     print('no error in received message')
# else:
#     print('position of error is', len(arr)-correction+1, 'from the left')

blocks = []
with open('dump.txt', 'r') as f:
    blocks = f.readlines()
blocks = [b.strip() for b in blocks]

m = 7
r = calc_redundant_bits(m)

idx = 0
repaired_blocks = []
for b in blocks:
    # if idx == 1:
    #     break
    chunks = [b[i:i+m] for i in range(0, len(b), m)]
    repaired_block = []
    for chunk in chunks:
        correction = detect_error(chunk, r)

        if correction == 0:
            print(chunk, '-> No error')
            repaired_block.append(chunk)
        else:
            c_idx = len(chunk)-correction
            fixed = [*chunk]
            fixed[c_idx] = '0' if fixed[c_idx] == '1' else '1'
            fixed = ''.join(fixed)
            print(chunk, '->', fixed, '  error is', c_idx+1, 'from the left')
            repaired_block.append(fixed)
    
    repaired_blocks.append(''.join(repaired_block))
    idx += 1

print('repaired blocks', repaired_blocks, '\n')

data_blocks = []
for block in repaired_blocks:
    chunks = [b[i:i+m] for i in range(0, len(b), m)]

    data_block = []
    for chunk in chunks:
        bits = [*chunk]
        # ham_out = p0 + p1 + d + p2 + c + b + a
        # data = bits[0] + bits[1] + bits[2] + bits[4]
        data = bits[4] + bits[2] + bits[1] + bits[0]
        data_block.append(data)
    data_blocks.append(''.join(data_block))

print(data_blocks, '\n')

# print('final\n', ''.join(data_blocks))

for i in data_blocks:
    print(i,'\n')

# [4<-0] 1001110101111001100101010101011111000111110010111100101111001100100110011000110010111001110101100001111100010000101000001101101110001000010011111101110011100001110001001010110001011000000110001000010010000101110111110000001111000000010111111101011111011000110010010100001111001111100100010001110010000101010101001111100010011000000100010101100100000011110111011000110101010111110111111000000110010011110100011101000111010001100001101101111110000001010011111000100001010111110010001101001111010001010111011100110111011111100000011100001000011010
# [4->0] 1001101111101001100110101010111000111110001111010011110100110011100110010001001111011001101101101000111110000000010100001011110100010001001011111011001101111000001100100101001110100001100000010001001000011010101111110000110000110000101011111011111010110001001110010010110000111111100110001000001100011010101000101111000110010001100010001010100100001100101110110001101110101110101111110001100010011100101110001011100010111000000101101011111100011000001011110001000110101110001100011011110010111000101010110011101110111111000110000011010010000101

# 011001100011110000011001000000000100001100011001010011000000111100011001010110100100110000010110011001100101010101001100011111110001011001001100011010010111000001011010010101010111000000001111001111000000000000001111011001100100001100111100000101100100001100100101000000000100110000100101001010100010010100101010001001010001011001101001001001010001011001110000000110010100110001101001001001010100110000000000001100110100110000111100000101100000111101001100000000000000000001010101011111110011110000000000000110010011110000000000000000000100001100011001011100000110011001100110001111000100001101101001011001100111000000011001010110100111111100100101000000000000000001111111000000000000111100010110000011110001100100011001010011000111000001011010011010010001011001001100000011110111111101101001011100000101101001101001011100000110100100011001011010010010010101010101001100110110100100010110010011000000111101100110001111000110011001000011000110010011001100001111000101100101101000110011000101100010101001111111000101100010010100010110011111110110100100110011010101010111000001111111000000000010010100011001011001100001011000110011010011000000000000111100001100110001100101001100010000110110011000001111000110010100001101001100010000110010101001110000
