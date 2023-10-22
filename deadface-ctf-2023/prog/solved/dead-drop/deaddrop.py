# Password recovery:
# buA9kvZ=T_A}b[J8l:@ob_tviPZtb_<olOpxkvZ=T_=xju]olOpxkvZ=T_bxlu]olOpxkvZ=QIEE

rec = 'buA9kvZ=T_A}b[J8l:@ob_tviPZtb_<olOpxkvZ=T_=xju]olOpxkvZ=T_bxlu]olOpxkvZ=QIEE'

arr = [
    'empty', 'interest', 'current', 'valuable', 'influence', 'from', 'scolded', 'would', 'got', 
    'key', 'facility', 'run', 'great', 'tack', 'scent', 'close', 'are', 'a', 'plan', 'counter', 
    'earth', 'self', 'we', 'sick', 'return', 'admit', 'bear', 'cache', 'to', 'grab', 'domination', 
    'feedback', 'especially', 'motivate', 'tool', 'world', 'phase', 'semblance', 'tone', 'is', 
    'will', 'the', 'can', 'global', 'tell', 'box', 'alarm', 'life', 'necessary'
]

def print_password(nums):
    if len(nums) < 1:
        print("Must provide a list of at least one number i.e. [1]")
    print("flag{{{}}}".format(" ".join([arr[num] for num in nums])))

def left_shift(s, n):
    return ''.join(chr(ord(char) - n) for char in s)

print(len(arr)) # 49

for i in range(1, 10):
    print(i, left_shift(rec, i))

# 8 Zm91cnR5LW9uZSB0d28gZWlnaHRlZW4gdGhpcnR5LW5pbmUgdGhpcnR5LWZpdmUgdGhpcnR5IA==
# fourty-one two eighteen thirty-nine thirty-five thirty 

# 41 2 18 39 35 30

print_password([41, 2, 18, 39, 35, 30])
