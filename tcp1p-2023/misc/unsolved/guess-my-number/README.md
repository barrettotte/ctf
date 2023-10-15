# guess-my-number

My friend said if i can guess the right number, he will give me something. Can you help me?

## Solution

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Misc/Guess%20My%20Number/writeup


- Crack the `rand()` function with the same seed (1337)
- Because `rand()` is executed once, the value is always same
- Calculate the exact key with the known value (`random & 0xcafebabe`)
- Use XOR to recover key

