"""
FINITE FIELDS ARITHMETIC
By Vincent Nguyen

* Support finite fields of orders:
    4, 5, 7, 8, 9, 16, 25, 27, 32, 49
* Irreducible polynomials stored in hash table

* Future todos:
    Can choose irreducible polynomials
    Raw_input option

For best experience, run interactive.ipynb to see 
interactive, dynamic arithmetic.

TO RUN WITHOUT IPYTHON NOTEBOOK:
>>> from finite_fields import poly
>>> O = "4"
>>> A = [1, 1]
>>> B = [1]
>>> poly(order = O, p1 = A, p2 = B).main()
======================================
ARITHMETIC IN FINITE FIELD OF ORDER 4
IRREDUCIBLE POLYNOMIAL 1 + x + x^2
======================================
1 + x = 1 + x
1 = 1
SUM: x
PRODUCT: 1 + x
MULTIPLICATIVE INVERSE OF 1 + x : x
MULTIPLICATIVE INVERSE OF 1 : 1
QUOTIENT: 1 + x
''

"""
from __future__ import print_function
from itertools import product
from collections import OrderedDict

class poly(object):
    def __init__(self, order = "4", p1 = [], p2 = []):
        """
        order : str
            specifies order of finite field
            
        p1 : lst
            polynomial representation in list structure
            
        p2 : lst
            polynomial representation in list structure
            
        irr_poly : dict
            (key, value) of finite field order :  resepctive
            tuple value of (irreducible polynomial, modular, degree)
        
        table : dict
            (key, value) of translated elements for finite field order :
            respective list structure of element
        """
        self.order = order
        self.p1 = p1
        self.p2 = p2
        
        #(irreducible polynomial, modulo, degree-1 of element)
        self.irr_poly = OrderedDict([('4',([1, 1, 1], 2, 2)),
                         ('5',([5], 5, 1)),
                         ('7', ([7], 7, 1)),
                         ('8', ([1, 1, 0, 1], 2, 3)),
                         ('9', ([1, 0, 1], 3, 2)),
                         ('16', ([1, 1, 0, 0, 1], 2, 4)),
                         ('25', ([3, 3, 1], 5, 2)),
                         ('27', ([1, 0, 2, 1], 3, 3)),
                         ('32', ([1, 0, 1, 0, 0, 1], 2, 5)),
                         ('49', ([3, 2, 1], 7, 2))])
    
        self.table = self.make_table()
        
    def get_table(self):
        """
        returns get_table 
        OrderedDict preserve order for dropdown representation
        """
        return OrderedDict([(self.translate(i), i) for i in self.table])        
        
    def get_irr_poly(self):
        """
        returns irr_poly dictionary
        OrderedDict preserve order for dropdown representation
        """
        return OrderedDict(self.irr_poly)
    
    def degree(self, p):
        """
        returns degree of polynomial
        """
        while p and p[-1] == 0:
            p.pop()
        return len(p)-1
    
    def simplified(self, p):
        """
        returns simplified result
        """
        #divide by irreducible polynomial
        reduced = self.div(p, self.irr_poly[self.order][0])[1]
        #apply modulo
        modded = [i % self.irr_poly[self.order][1] for i in reduced]
        return modded
    
    def add(self, p1, p2):
        """
        returns sum of two polynomials
        Hackish fix for zero elements since they are empty due to self.degree popping
        """
        if len(p1) == 0:
            p1 = [0]
        if len(p2) == 0:
            p2 = [0]
        #ensures polynomials are same length
        if len(p1) > len(p2):
            for _ in xrange((len(p1) - len(p2))):
                p2.append(0)
        elif len(p1) < len(p2):
            for _ in xrange((len(p2) - len(p1))):
                p1.append(0)
        return self.simplified([sum(x) for x in zip(p1, p2)])
        

    def mult(self, p1, p2):
        """
        returns product of two polynomials
        Hackish fix for zero elements since they are empty due to self.degree popping
        """
        if p2 is None:
            return None
        if len(p1) == 0:
            p1 = [0]
        if len(p2) == 0:
            p2 = [0]
        product = [0]*(len(p1) + len(p2) - 1)
        for i, j in enumerate(p1):
            for k, l in enumerate(p2):
                product[i+k] += j*l
        return map(int, self.simplified(product))

    def div(self, N, D):
        """
        http://rosettacode.org/wiki/Polynomial_long_division#Python
        """
        dD = self.degree(D)
        dN = self.degree(N)
        
        #if just degree 0 on numerator than always return numerator
        if dN == 0 and dD != 0:
            return None, N
        
        #only for orders 5 and 7 since they consist of just natural numbers
        if (dD and dN) == 0 or self.order == (5 or 7):
            if len(D) == 0:
                D = [0]
            if len(N) == 0:
                N = [0]
            return None, [N[0] % D[0]]
        if dD < 0: raise ZeroDivisionError
        if dN >= dD:
            q = [0] * dN
            while dN >= dD:
                d = [0]*(dN - dD) + D
                mult = q[dN - dD] = N[-1] / float(d[-1])
                d = [coeff*mult for coeff in d]
                N = [( coeffN - coeffd ) for coeffN, coeffd in zip(N, d)]
                dN = self.degree(N)
            r = N
        else:
            q = [0]
            r = N
        return q, r
    
    def translate(self, p):
        """
        returns string representation of polynomial from list structure
        """
        if p is None:
            return "Undefined"
        
        while p and p[-1] == 0:
            p.pop()
        s = ""
        if len(p) == 0:
            return "0"
        for i,n  in enumerate(p):
            if i != 0:
                if i != 1:
                    if n != 0:
                        if n != 1:
                            s += str(n) + "x" + "^" + str(i)
                        else:
                            s += "x" + "^" + str(i)
                else:
                    if n != 0:
                        if n != 1:
                            s += str(n) + "x"
                        else:
                            s += "x"
            else:
                if n != 0:
                    s += str(n)
                
            if i != len(p) - 1 and n != 0:
                s += " + "
        return s

    def make_table(self):  
        """
        returns all elements in finite field
        """
        table = []
        x = [i for i in xrange(int(self.irr_poly[self.order][1]))]
        table = [ list(p) for p in product(x, repeat=self.irr_poly[self.order][2])]
        return table
    
    def find_mult_inverse(self, p):
        """
        returns multiplicative inverse of polynomial or None for zero element
        """
        for i in self.table:
            prod = self.mult(p,i)
            while prod and prod[-1] == 0:
                prod.pop()
            if prod == [1]:
                return self.simplified(i)
                break
        return None
            
    def main(self):
        #simplifies representation of polynomial (only applicable for user input since dropdowns
        #confines what elements can be chosen)
        _p1 = self.simplified(self.p1)
        _p2 = self.simplified(self.p2)
        
        summ = self.add(_p1, _p2)
        product = self.mult(_p1, _p2)
        mult_inverse1 = self.find_mult_inverse(_p1)
        mult_inverse2 = self.find_mult_inverse(_p2)
        quotient = self.mult(_p1, mult_inverse2)
        
        print("======================================")
        print("ARITHMETIC IN FINITE FIELD OF ORDER %s" % self.order)
        print("IRREDUCIBLE POLYNOMIAL %s" % self.translate(self.irr_poly[self.order][0]))
        print("======================================")
        print(self.translate(self.p1), "=", self.translate(_p1))
        print(self.translate(self.p2), "=", self.translate(_p2))
        print
        print("SUM:", self.translate(summ))
        print("PRODUCT:", self.translate(product))
        print("MULTIPLICATIVE INVERSE OF", self.translate(self.p1), ":", self.translate(mult_inverse1)) 
        print("MULTIPLICATIVE INVERSE OF", self.translate(self.p2), ":", self.translate(mult_inverse2))
        print("QUOTIENT:", self.translate(quotient))
        
        return ""