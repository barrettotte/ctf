import os
import subprocess
from zipfile import ZipFile

total_zips = 25000
out_dir = './unzipped'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

i = total_zips
while i > 0:
    zip_dir = '.' if i == total_zips else out_dir

    with open(zip_dir + '/password.txt', 'r') as f:
        password = f.readline().strip()

    zip_name = f'{zip_dir}/zip-{i}.zip'
    print('unzipping', zip_name, 'with password', password)

    # extremely slow... https://stackoverflow.com/questions/25600432/python-zipfile-module-extracts-password-protected-zips-slowly
    # with ZipFile(zip_name) as zf:
    #     zf.extractall(path=out_dir, pwd=password.encode('utf-8'))

    subprocess.call(['unzip', '-o', '-P', password, '-d', out_dir, zip_name])
    subprocess.call(['rm', zip_name])

    i -= 1
