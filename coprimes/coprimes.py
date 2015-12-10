import pandas as pd
import numpy as np
from collections import Counter

def gcd(a, q):
    r = a%q
    if r == 0:
        return q
    return gcd(q, r)

def order(a, i):
    n = 0
    flag = True
    while flag:
        n += 1
        if (i**n)%a == 1:
            flag = False
    return n

if __name__ == "__main__":
    a = int(raw_input("a: "))

    co_prime = [i for i in xrange(1, a) if gcd(a, i) == 1]

    table = np.array([[(i*j)%a for i in co_prime] for j in co_prime])
    header = [str(i) for i in co_prime]

    print
    print "***********************************************"
    print "*** MULTIPLICATION TABLE FOR COPRIMES OF %d ***" % a
    print "***********************************************"
    pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])
    with pd.option_context('display.max_rows', 50, 'display.max_columns', 50):
        print pd.DataFrame(table, header, header)

    print
    print "***********************************************"
    print "*** ELEMENT ORDER FOR COPRIME ELEMENT OF %d ***" % a
    print "***********************************************"

    orders = np.array([[order(a, i)] for i in co_prime])
    print pd.DataFrame(orders, index = co_prime, columns=["Order"])