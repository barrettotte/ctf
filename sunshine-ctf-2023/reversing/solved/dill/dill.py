# Source Generated with Decompyle++
# File: dill.cpython-38.pyc (Python 3.8)


class Dill:
    prefix = 'sun{'
    suffix = '}'
    o = [
        5,
        1,
        3,
        4,
        7,
        2,
        6,
        0]
    
    def __init__(self = None):
        self.encrypted = 'bGVnbGxpaGVwaWNrdD8Ka2V0ZXRpZGls'

    
    def validate(self = None, value = None):
        if not value.startswith(Dill.prefix) or not value.endswith(Dill.suffix):
            print("bad prefix/suffix")
            return False

        # value = None[len(Dill.prefix):-len(Dill.suffix)]
        value = value[len(Dill.prefix):-len(Dill.suffix)]
        print('debug [1]:', value, '->', len(value))

        if len(value) != 32:
            print("inner part of flag is not 32 characters")
            return False
        
        # original decompiled
        # c = (lambda .0 = None: [ value[i:i + 4] for i in .0 ])(range(0, len(value), 4))
        # value = None((lambda .0 = None: [ c[i] for i in .0 ])(Dill.o))

        c = (lambda x: [ value[i:i + 4] for i in x ])(range(0, len(value), 4))
        print('debug [2]: c =    ', c)

        value = ((lambda y: [ c[i] for i in y ])(Dill.o))
        print('debug [3]: value =', value)

        value = ''.join(value)

        print('debug [4]: value =', value)
        print('debug [5]: encrypted =', self.encrypted)
        print('debug [6]:', value == self.encrypted)
        
        if value != self.encrypted:
            return False

if __name__ == '__main__':
    # sun{?}
    # flag = "sun{testABCDEFGHIJKLMNOPQRSTUVWXYZ!@}"
    flag = "sun{ZGlsbGxpa2V0aGVwaWNrbGVnZXRpdD8K}"

    dill = Dill()
    valid = dill.validate(flag)
    
    print('------------------------')
    print('valid?', valid)

    if valid is None:
        print(flag, 'is the flag')
    else:
        print(flag, 'is not the flag')

#                        0      1       2       3       4       5       6       7
# debug [2]: c     = ['test', 'ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST', 'UVWX', 'YZ!@']
# debug [3]: value = ['QRST', 'ABCD', 'IJKL', 'MNOP', 'YZ!@', 'EFGH', 'UVWX', 'test']

# o = [5,1,3,4,7,2,6,0]

# v -> c
# [7,1,5,2,3,0,6,4]

# encrypted -> bGVnbGxpaGVwaWNrdD8Ka2V0ZXRpZGls

# 0    1    2    3    4    5    6    7
# bGVn bGxp aGVw aWNr dD8K a2V0 ZXRp ZGls

# reverse mapping
# ZGls bGxp a2V0 aGVw aWNr bGVn ZXRp dD8K

# ZGlsbGxpa2V0aGVwaWNrbGVnZXRpdD8K

# expected -> 
# actual   -> bGVnbGxpaGVwaWNrdD8Ka2V0ZXRpZGls

# cyberchef -> base64 on ZGlsbGxpa2V0aGVwaWNrbGVnZXRpdD8K
# dilllikethepicklegetit?

# sun{dilllikethepicklegetit?}
# not the flag?

# actually just the unencrypted -> sun{ZGlsbGxpa2V0aGVwaWNrbGVnZXRpdD8K}
