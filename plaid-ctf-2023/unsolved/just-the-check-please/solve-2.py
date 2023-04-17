import sys

PIE_BASE = 0x555555554000

breakpoints = [0xec56]

gdb.execute('file check')
gdb.execute('set pagination off')

for bp in breakpoints:
    gdb.execute(f'b *{PIE_BASE + bp}')

flag = ['_'] * 16
index = 0

while True:
    if flag[index] != '_':
        index = (index + 1) % 16
        continue

    counts = []
    for ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-':
        flag[index] = ch

        gdb.execute(f'starti "{"".join(flag)}"')

        count = 0
        while True:
            try:
                gdb.execute('c')
            except:
                break
            count += 1
        
        sys.stderr.write(f'ATTEMPT FLAG:{"".join(flag)}, COUNT:{count}\n')

        counts.append((count, ch))
    
    flag[index] = '_'
    if len(set(map(lambda x: x[0], counts))) != 1:
        flag[index] = sorted(counts, key=lambda x: x[0], reverse=True)[0][1]
        sys.stderr.write(f'CURRENT FLAG: {"".join(flag)}\n')
    
    index = (index + 1) % 16