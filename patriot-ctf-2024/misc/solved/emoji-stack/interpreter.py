TEST_SRC = '👍🔁47💬👉👍🔁68💬👉👍🔁20💬'

OP_RIGHT = 0
OP_LEFT = 1
OP_INC = 2
OP_DEC = 3
OP_PRINT = 4
OP_LOOP = 5

emoji_dict = {
    '👉': OP_RIGHT,  # 👉: Move the stack pointer one cell to the right
    '👈': OP_LEFT,   # 👈: Move the stack pointer one cell to the left
    '👍': OP_INC,    # 👍: Increment the current cell by one, bounded by 255
    '👎': OP_DEC,    # 👎: Decrement the current cell by one, bounded by 0
    '💬': OP_PRINT,  # 💬: Print the ASCII value of the current cell
    '🔁': OP_LOOP    # 🔁##: Repeat the previous instruction 0x## times
}

class EmojiMachine:
    def __init__(self) -> None:
        self.cells = [0] * 256
        self.sp = 0
        self.prev_fn = None

    def left(self):
        self.sp -= 1
        self.prev_fn = self.left

    def right(self):
        self.sp += 1
        self.prev_fn = self.right

    def inc(self):
        self.cells[self.sp] += 1
        if self.cells[self.sp] > 255:
            self.cells[self.sp] = 255

        self.prev_fn = self.inc
    
    def dec(self):
        self.cells[self.sp] -= 1
        if self.cells[self.sp] < 0:
            self.cells[self.sp] = 0

        self.prev_fn = self.dec

    def out(self):
        print(chr(self.cells[self.sp]), end='')
        self.prev_fn = self.out
    
    def loop(self, count: int):
        i = 0
        while i < count:
            if self.prev_fn:
                self.prev_fn()
            else:
                print('warn: loop has no func to run')
                break
            i += 1
        self.prev_fn = None

def parse(src: str) -> list:
    tokens = []
    i = 0
    while i < len(src):
        opcode = emoji_dict[src[i]]
        t = {'opcode': opcode, 'symbol': src[i]}

        if opcode == OP_LOOP:
            i += 1 # consume loop opcode

            # get loop iterations
            literal = ''
            while src[i].isalnum():
                literal += src[i]
                i += 1
            t['literal'] = f'0x{literal}'
            i -= 1 # backup to non-literal        

        tokens.append(t)
        i += 1

    return tokens

# src = TEST_SRC
with open('input.txt', 'r') as f:
    src = ''.join(f.readlines())

tokens = parse(src)
print(len(tokens), 'tokens')

# The Emoji Stack is 256 cells long, with each cell supporting a value between 0 - 255.
em = EmojiMachine()

for t in tokens:
    # print(f'interpreting {t}')

    if t['opcode'] == OP_RIGHT:
        em.right()
    elif t['opcode'] == OP_LEFT:
        em.left()
    elif t['opcode'] == OP_INC:
        em.inc()
    elif t['opcode'] == OP_DEC:
        em.dec()
    elif t['opcode'] == OP_PRINT:
        em.out()
    elif t['opcode'] == OP_LOOP:
        em.loop(int(t['literal'], 16))

    # print('sp =', em.sp)
    # for i, c in enumerate(em.cells):
    #     if c > 0:
    #         print(f'cells[{i}] = {c}')
    # print('----------------------------')
