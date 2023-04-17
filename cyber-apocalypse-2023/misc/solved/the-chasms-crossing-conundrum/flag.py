# ripped algorithm from https://github.com/murdesi/bridge-crossing

from pwn import *
import itertools

crossing_time = {}

def move_single(src, dst, p, time_taken, solution, solution_set):
    dst.remove(p)
    src.append(p)
    time_taken += crossing_time[p]
    solution += ',[' + str(p+1) + '],'
    solve(src[:], dst[:], time_taken, solution, solution_set)

def move_pair(src, dst, node, time_taken, solution, solution_set):
    if len(src) == 0:
        return

    x, y = (node[0], node[1])
    src.remove(x)
    src.remove(y)
    dst.append(x)
    dst.append(y)
    time_taken += max(crossing_time[x], crossing_time[y])
    solution += '[' + str(x+1) + ',' + str(y+1) + ']'

    if len(src) == 0:
        # print('solution=' + solution, '; time =', time_taken)
        solution_set.append((solution, time_taken))
        return
    for l in dst:
        move_single(src[:], dst[:], l, time_taken, solution, solution_set)


def solve(src, dst, time_taken, solution, solution_set):
    if len(src) == 0:
        return
    ct = []
    for x, y in itertools.combinations(src, 2):
        ct.append((x, y))
    for node in ct:
        move_pair(src[:], dst[:], node, time_taken, solution, solution_set)

#############################################

io = remote('165.227.224.40', 30001)

io.recvuntil(b'>')
io.sendline(b'2')
io.recvuntil(b'flashlight.')
people_raw = io.recvuntil(b'flashlight')

people_lines = list(filter(None, people_raw.decode().split('\n')))[:-1]
people = [{'i': str(i+1), 't': int(line.split(' ')[4])} for i,line in enumerate(people_lines)]
flashlight = io.recvuntil(b'.').decode().split(' ')[-2]

# only brute force for small person count
if len(people) > 6:
    print('Too large, ' + str(len(people)) + ' people')
    exit(1)

print(io.recvuntil(b'> '))

# people_times = [78,73,48,90,74,99] # 606
people_times = [p['t'] for p in people]
# people_times.sort()

src = []
for x in range(0, len(people_times)):
    src.append(x)
    crossing_time[x] = int(people_times[x])

print(src)
print(crossing_time)
solution_set = []
solve(src[:], [], 0, '', solution_set)
solution = sorted(solution_set, key=lambda x: x[1])[0]

print('DONE\nPeople:')
for person in people:
    print('  Person', person['i'], ': ', person['t'], 'minutes')
print('Flashlight: ' + str(flashlight))
print('\nSolution: ', solution[0])
print('Total Time: ', solution[1], 'min\n')

# payload = b'[1,2],[1]'
payload = str.encode((''.join(solution[0])))
io.sendline(payload)

# get flag
try:
    print(io.recvline(20))
except EOFError:
    pass
io.interactive()

