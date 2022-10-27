# from secret import FLAG
import binascii
from hashlib import sha512
import socketserver
import signal
from random import randint

WELCOME = """
**************** Welcome to the Hash Game. ****************
*                                                         *
*    Hash functions are really spooky.                    *
*    In this game you will have to face your fears.       *
*    Can you find a colision in the updated sha512?       *
*                                                         *
***********************************************************
"""


class ahs512():

    def __init__(self, message):
        print(f'\ncalculating hash for {message}...')
        print('  message length =', len(message))
        self.message = message
        self.key = self.generateKey()

    def generateKey(self):
        print('  generating key...')
        while True:
            key = randint(2, len(self.message) - 1)
            if len(self.message) % key == 0:
                break
        print(f'  {key=}')
        return key

    def transpose(self, message):
        print('  transposing...')

        transposed = [0 for _ in message]
        columns = len(message) // self.key

        for i, char in enumerate(message):
            row = i // columns
            col = i % columns
            transposed[col * self.key + row] = char

        return bytes(transposed)

    def rotate(self, message):
        print('  rotating...')
        return [((b >> 4) | (b << 3)) & 0xff for b in message]

    def hexdigest(self):
        print(f'  digesting...')

        transposed = self.transpose(self.message)
        print('transposed =', [b for b in transposed])
        
        rotated = self.rotate(transposed)
        print('  rotated =', rotated)
        
        x = sha512(bytes(rotated)).hexdigest()
        print(f'done. hash = {x}')
        return x

def main():
    print(WELCOME)

    original_message = b"pumpkin_spice_latte!"
    original_digest = ahs512(original_message).hexdigest()
    # print(f"\nFind a message that generate the same hash as this one: {original_digest}\n")

    try:
        # message = input("\nEnter your message: ")
        message = bytes.fromhex(b'Who drank my beer?'.hex())

        digest = ahs512(message).hexdigest()

        if ((original_digest == digest) and (message != original_message)):
            # sendMessage(s, f"\n{FLAG}\n")
            print(f'FLAG GOT!!!!\n')
        else:
            print("\nConditions not satisfied!\n")

    except KeyboardInterrupt:
        print("\n\nExiting")
        exit(1)

    except Exception as e:
        print(f"\nAn error occurred while processing data: {e}\n")


if __name__ == '__main__': main()
