from pwn import *
from hashlib import sha256, md5
# from _md5 import md5  # apparently faster than hashlib?
import multiprocessing as mp
import itertools
from more_itertools import ichunked
import time

# note: only have 15 seconds

def check_md5(msg, target):
    if md5(msg.encode('utf-8')).hexdigest() == target:
        return msg
    return None

def message_generator(alphabet):
    for msg in itertools.product(alphabet, repeat=128):
        yield ''.join(msg)

def find_md5_msg(alphabet, target_hash, max_hashes):
    hash_count = 0
    for msg in message_generator(alphabet):
        if check_md5(msg, target_hash):
            return msg
        if hash_count % 1000000 == 0 and hash_count > 0:
            print(f'checked {hash_count} ({(hash_count/max_hashes):.25f}%)')
        hash_count += 1 
    return None

def check_md5_parallel(msg, target_hash, found, lock):
    if found.value:
        return None # already found, no work
    if md5(msg.encode()).hexdigest == target_hash:
        with lock:
            found.value = 1
        return msg
    return None

def find_md5_msg_parallel(alphabet, target_hash):
    msg = None
    found = mp.Value('i', 0)
    lock = mp.Lock()

    with mp.Pool(maxtasksperchild=10) as pool:
        results = pool.starmap(check_md5_parallel, ((msg, target_hash, found, lock) for msg in message_generator(alphabet)), chunksize=10)
        msg = next(filter(lambda x: x is not None, results.get()))
    return msg

def dummy_func(msg, target_hash):
    return (msg, target_hash)

def find_md5_msg_parallel_2(alphabet, target_hash):
    msg = None
    # found = mp.Value('i', 0)
    # lock = mp.Lock()
    # args = (target_hash, found, lock)

    hash_len = 12
    combinations = itertools.product(alphabet, repeat=hash_len)
    print(f'Checking {(len(alphabet)**hash_len):,} hashes...')

    i = 0
    with mp.Pool() as pool:
        args = [(x, target_hash) for x in combinations]
        # for result in pool.starmap(dummy_func, args, chunksize=10000):
        #     i += 1
        res = pool.map_async(dummy_func, args)
        res.get()
    print(f'checked {i:,} hashes')

    return msg

def main():
    total_len = 263
    prefix_len = 135
    alphabet = '☊☋☌☍'
    target_hash = '3bc33aacbcae59c2707b61da18a25d2a'
    max_hashes = len(alphabet)**(total_len-prefix_len)
    original_msg = None

    # combinations = itertools.product(alphabet, repeat=128) # reset
    # batches = ichunked(combinations, 100000)
    
    print('finding original message...')
    start_time = time.time()

    # find_md5_msg(alphabet, target_hash, max_hashes)
    # find_md5_msg_parallel(alphabet, target_hash)
    find_md5_msg_parallel_2(alphabet, target_hash)

    print(f'finished in {(time.time() - start_time):.2f} seconds')
    if not original_msg:
        raise Exception("Did not find original message...")
    print(f"Found original message! {original_msg}")

    exit(0)

    io = process('./server.sh')
    # io = remote('167.99.200.95', 30543)

    line = io.recvline().decode().split(' ')
    target = line[6] # 10 chars
    target_len = 18

    print("random prefix -> ", target)
    alphabet = string.ascii_letters + string.digits

    pow_msg = None
    pow_hash = None
    start_time = time.time()

    hash_count = 0
    for combo in itertools.product(alphabet, repeat=8):
        s = ''.join(combo)
        msg = target + s
        msg_hash = sha256(msg.encode('ascii')).hexdigest()
        # print(f"'{msg}' -> {msg_hash}")

        if hash_count > 0 and hash_count % 10000000 == 0:
            print(f'checked {hash_count} hashes')

        if msg_hash[-6:] == 'ffffff':
            pow_msg = msg
            pow_hash = msg_hash
            break
        hash_count += 1

    if pow_msg is None or pow_hash is None:
        raise Exception("Could not calculate proof of work...")

    elapsed = time.time() - start_time
    print(f'found in {elapsed} second(s)')
    print(f'processed {hash_count} hashes')
    print(f'pow hash -> {pow_hash}')
    print(f'pow message -> {pow_msg}')

    # input proof_of_work to server
    io.sendline(pow_msg.encode('ascii'))

    print(io.recvline()) # b'which phase? [new moon, waxing crescent, waxing gibbous, full moon]\n'
    io.sendline(b'waxing crescent')

    print(io.recvline()) # b'waxing crescent: trial 1/50\n'
    print(io.recvline().decode())  # encoded
    print(io.recvline().decode())  # md5 hash
    print(io.recvline().decode())  # ❓️

    io.sendline(b'test')
    print(io.recvline()) # echos
    print(io.recvline().decode()) # ❌ or ✅
    print(io.recvline().decode()) # fail reason  ⌛️❗️or 🔮️🚫️❗️

if __name__ == '__main__':
    main()