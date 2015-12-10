"""

==================
Euclid GCD
by Vincent Nguyen
==================

Computes the greatest common divisor beteween two integers between 2 and 2**16+1, the
Fermet prime.  Returns the GCD and integers m and n such that ma+nb = GCD

Inputs
------------------
a: int
    Integer between 2 and 65537
    Ex.) 37

Examples
------------------
a: 4
>> GCD(4, 2) = 2 = 1 x 2 + 0 x 4

"""

from random import randint

def euclid_for(a, q):
    coefs = []
    def gcd(a, q): 
        b, r = a/q, a%q
        coefs.append((a, b, q, r))
        if r != 0:
            return gcd(q, r)
    gcd(a, q)
    #assert(coefs[-1][2] == 1)
    return coefs

def euclid_back(eqs):
    if len(eqs) == 1:
        return (eqs[0][2], 1, eqs[0][2], eqs[0][3], eqs[0][0])
    t = (eqs[-2][3], 1, eqs[-2][0], -1*eqs[-2][1], eqs[-2][2])
    for i in xrange(len(eqs)-2):
        cur = eqs[len(eqs)-i-3]
        t = (t[0], t[3], cur[0], t[1] - t[3]*cur[1], t[2])
    assert(t[0] == t[1]*t[2]+t[3]*t[4])
    return t

if __name__ == "__main__":
    a = int(raw_input("a: "))
    b = 2**16+1

    if a > 1 and a < 2**16 + 1:
        eqs = euclid_for(a, b)
        tup = euclid_back(eqs)
        print
        print "GCD(%d, %d) = %d = %d x %d + %d x %d" % \
            (a, b, eqs[-1][2], tup[1], tup[2], tup[3], tup[4])
        prime = tup[1]
        if prime < 0:
             prime += 2**16+1
        assert(prime * tup[2] % tup[4] == 1 and prime > 1 and prime < 2**16+1)
        print "(%d)(%d) = 1" % (a, prime)