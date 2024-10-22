
with open('encrypted.txt', 'r') as f:
    s = f.read().split(' ')

print(s)

words = []

for w in s:
    word = ''
    
    for b in w:
        word += '0' if b == '\\' else '1'

    word = chr(int(word, 2))
    words.append(word)

print(''.join(words))

