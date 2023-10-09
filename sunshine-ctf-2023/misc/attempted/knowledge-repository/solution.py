import hashlib
import os
import shutil

def sha256_hash_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

base_directory = './morse-files'
file_paths = []
file_hashes = []

for root, dirs, files in os.walk(base_directory):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        file_paths.append(file_path)

i = 0
prev_hash = ''
for f in sorted(file_paths):
    sha256_hash = sha256_hash_file(f)
    # print(f"File: {f}, SHA-256 Hash: {sha256_hash}")
    file_hashes.append({'f': f, 'h': sha256_hash})
    i += 1

print('checked', i, 'file(s)')
file_hashes = sorted(file_hashes, key=lambda x: x['f'])
unique_values = [d['h'] for d in file_hashes]
unique_values = set(unique_values)
print(len(unique_values), 'unique hashes')

hash_lookup = {
    '187538722b97c4f4542d63e9c818241b337adfd1fab90f30de81bf913f76818d': 'D',
    'ee9cfda63c0db181610260c8ea91e662d2fec68acebf49dcc2f39f8ab8bf806a': '6',
    '246b30ac2b04283b6f0481551883a4c0f5599bcbf461c11750af2ae3a7ebb76f': 'F',
    'eeb4da53378e5a6ecb8386016c180e48909a77500be3394f4a94dd0cf96b5b89': 'Q',
    '8358672e28d718809fb46845ecd79af3ec0551ac4a2087c8e9d329fa8a4aed49': 'A',
    '7e2e5aef043f86bc96795c8e749cc41e0abcfd28fdd13e1462c945f541bcafad': '5',
    'ac201ae7a99149352f34b12ebd5e2cb40ebce9e33970a2145f53db5dc8cd9b90': 'Z',
    'b1eb5beb2cf7e864d58fdb93d01f8f5cf9e051e5673728ad8951adb34451e9d7': 'P',
    'a568aa9781e56f96fb59efc3022c2365d8fe494ab34da62317b467981c80d356': 'G',
    'c34056558e2946f5e531a98bff36e85fb73f92784fce4f6235907aa6079ed91d': 'I',
    '0f132a5074b472474233cf0e56bf207179e543364348f36068e360290f57a528': 'H',
    'c6f80a968c095f4265b31e06fed5d0da6980504826ec843c6a6c275119caae77': '7',
    'c9286a01da169cb6a65e20a5a9fa4e4c17805112f22f8ce4145d042222e45ecd': 'R',
    'e43d36d79c2740853995cbcde88bf6b92c960bdb294ea0d9fd943742b25020fb': 'V',
    '7a787aff8cab4fa4388a0b9fd00a1f5add033375383146ef8fd59a2647b6e935': 'L',
    '6db83b2193b2c701b15b00d4ed6282dbda46a2b80de4dcc9008a14efcf8cc8db': '3',
    '69dbe0a99626e8bcd572398a28e2f1993b198365fa904df9b55102f9f91a661a': 'Y',
    '4f40572b9c2eca86a9ee0caa1e205a8e9bf42b36b834d82c204ae1668a30dca5': 'J',
    '084c0d2dc2c35296b72fc73326060c783deca76f1d68f0863829e99125701d71': 'T',
    '474ecd5d554fdf9c64212b751b949641c13a6b32ff0b8d61d42da401eea539f7': 'O',
    '87f677ed2a1f8c89ff1258cfcdedf94d69e8b843606353a806676bb9a07a80c2': '2',
    'c68bb6e68070f4406029065555aa4dd90241045982622576c945f0c41d3bb0d6': 'B',
    'cd5893dda87b7cd3c2b1fa0e0bf30fa1e0e9c04fdfa4827e43937254bc865507': 'W',
    '317b0a4aea65c5485590a52e6fe53e46e6e623fec0b5bf48df164ce76f2a0d54': 'E',
    'ea90792d9865ff7831557aa09fd32232a179c2b017a266b1052159b651385a7d': 'X',
    'b73568b85e3d394cea440eca9ffb521865d7f58bee1772a873b18a81929633e6': 'K',
    'd9125c7917a1127cd8310c89d71ba938b1d4cb0bc6d02eb57cb8d8017bd430b3': 'C',
    '24b903dab3a7761174f363ba6e2a584f3cd2ebca7e1cd5c1153446784860d28e': 'N',
    '69221c7871f47fec9e6542769b2900d48ca152a4f2380a3126a7fc83674b359a': 'U',
    'bbdfb8744b46b6f315b388fa74992da183620462a32be3df3e23c3e5d94a9347': 'S',
    'b9b3ac17393ae8acfdbc033cb2074c319239a793c62dc0b5c88279ce2d0dca68': '4',
    '22f743f81916b1be2ce4e2bb16c145d28ca337552fdf38f6a5ce3e01e333853a': 'M',
    '01c4d529eb2b557b2c08b20838081b100172c052f0d3af58c38d89b6916887b3': '=',
}

print('working on', len(file_hashes), 'hashes')

# file_hashes = sorted(file_hashes, key=lambda x: x['f'], reverse=True)

prev_hash = ''
payload = []
for d in file_hashes:
    if d['h'] not in payload:
        payload.append(d['h'])
    # if d['h'] != prev_hash:
    #     c = hash_lookup[d['h']]
    #     payload.append(c)
    #     prev_hash = d['h']

print(len(payload))
# print(''.join(payload))

payload = ''.join([hash_lookup[h] for h in payload])
# payload = payload[::-1]
print(payload)
