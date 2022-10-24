from Crypto.Util.number import isPrime

# n = 300
def generate_basis(n):
    basis = [True] * n

    # n**0.5 = int(17.32) = 17 + 1 = 18
    for i in range(3, int(n**0.5) + 1, 2):
        if basis[i]:
            basis[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if basis[i]]


# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html
# https://en.wikipedia.org/wiki/Carmichael_number
# https://en.wikipedia.org/wiki/Strong_pseudoprime
# https://oeis.org/A074773/a074773.txt
#
# n is prime if and only if the solutions of x^2 = 1 (mod n) 
#   are x = +- 1
# 
def millerRabin(n, b):  # n = p, b = 300  ... b also determines accuracy ?? - prime bases
    basis = generate_basis(300)
    
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # r, s = 0, n - 1
    r = 0
    s = n - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for b in basis:
        x = pow(b, s, n) # b^s mod n = 300^s mod n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n) # x^2 mod n
            if x == n - 1:
                break
        else:
            return False
    return True


def _isPrime(p):
    if p < 1:
        return False
    if (p.bit_length() <= 600) and (p.bit_length() > 1500):
        return False
    if not millerRabin(p, 300):
        return False

    return True


def main(s):
    p=s
    try:
        p = int(p)
    except:
        print(s, "Error!")

    if _isPrime(p) and not isPrime(p):
        raise Exception('FLAG GOT! => ' + str(p))
    else:
        print(s, "Conditions not satisfied!")

if __name__ == '__main__':
    print()
    
    basis = generate_basis(300)
    print('\n'.join([str(b) for b in basis]))
    main('')



    # was worth a shot
    # with open('carmichael_16757.txt', 'r') as f:
    #     for line in f.readlines():
    #         print(line)
    #         main(line.split(' ')[1])

    # https://rosettacode.org/wiki/Carmichael_3_strong_pseudoprimes

    # need to find carmichael number which passes miller-rabin, but isn't prime
    # it needs to be a strong pseudo prime for all bases under 300

    # a^n = a (mod n) for every int 1 <= a <= n ; carmichael numbers
    # smallest:   561 = 3 * 11 * 17

    # https://math.stackexchange.com/questions/1500827/efficient-method-to-find-the-strong-pseudoprimes-to-base-2-3-5-upto-109
    # https://www.ams.org/journals/mcom/2001-70-234/S0025-5718-00-01215-1/S0025-5718-00-01215-1.pdf
    # https://math.stackexchange.com/questions/1502172/constructing-a-number-strong-probable-prime-to-several-bases
    # *https://github.com/danaj/Math-Prime-Util-GMP/blob/master/t/17-pseudoprime.t
    # *https://www.ams.org/journals/mcom/1995-64-209/S0025-5718-1995-1260124-2/S0025-5718-1995-1260124-2.pdf
    # *https://mathcrypto.wordpress.com/2014/11/23/large-examples-of-strong-pseudoprimes-to-several-bases/
    #   - the implementation of the strong probable prime test must be randomized

    # number from Arnault F 1995. 397 digit carmichael number that is a strong pseudoprime to all 62 bases under 300.
    # 2887148238050771212671429597130393991977609459279722700926516024197432303799152733116328983144639225941977803110929349655578418949441740933805615113979999421542416933972905423711002751042080134966731755152859226962916775325475044445856101949404200039904432116776619949629539250452698719329070373564032273701278453899126120309244841494728976885406024976768122077071687938121709811322297802059565867
