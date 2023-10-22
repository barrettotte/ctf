# 0. purple = 6E309E
# 1. green = 31AC53
# 2. pink = FB56FB
# 3. black = 000000

img = [
    '01010100',
    '00213022',
    '32030311',
    '32032300',
    '02001123',
    '00110003',
    '01003212',
    '00120331',
]

lookup = {
    '0': '6E309E',
    '1': '31AC53',
    '2': 'FB56FB',
    '3': '000000',
}

decoded = []
for line in img:
    for c in line:
        decoded.append(lookup[c])

with open('decoded.txt', 'w+') as f:
    f.write(''.join(decoded))
