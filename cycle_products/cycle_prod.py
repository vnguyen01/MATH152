"""

==================
CYCLE PRODUCTS
by Vincent Nguyen
==================

Computes the product for permutations 'a' and 'b'.  Displays the result of
'ab', 'ba', 'aba^-1', and 'bab^-1'.  I used dictionaries to indicate mappings.

Inputs
------------------
a: string, default "(I)"
    Permutation of 1...9 represented in cycle notation with (...)
    Ex.) (145)(26)

b: string, default "(I)"
    Permutation of 1...9 represented in cycle notation with (...)
    Ex.) (145)(26)

Examples
------------------
p1 = "(234)(12354)"
p2 = "(123)(456721)(45391)"

perm_mult(p1, p2)

>> a =  (13524)
>> b =  (15)(39467)
>> a^-1 =  (14253)
>> b^-1 =  (15)(37649)
>> ab =  (12467539)
>> ba =  (19452673)
>> aba^-1 =  (16759)(23)
>> bab^-1 =  (12659)

Error support
------------------
Parentheses to indicate cycle beginning and end
Checks for duplicate values within cycle
Only numbers within cycle

"""

import re 

#swaps keys and values of dictionary for inverse computation
def swap(dic):
    return {v: k for k, v in dic.items()}

#computes dictionary mapping for a single cycle
def product(cycle):
    if len("".join(set(cycle))) != len(cycle):
        raise ValueError("Duplicate values in cycle!")
    if not cycle.isdigit():
        raise ValueError("Only numbers permitted in cycle!")
        
    mapping = {str(i): str(i) for i in xrange(1, 10)}
    if cycle != "I":
        for i in xrange(len(cycle)):
            n1 = cycle[i]
            n2 = cycle[i+1] if i+1 != len(cycle) else cycle[0]
            mapping[n1] = n2
    return mapping

#goes through final dictionary mapping to identify cycles
def path(final):
    lst = []
    nums = [str(i) for i in xrange(1, 10)]
    while len(nums) != 0:
        i, s = nums[0], nums[0]
        pointer = final[nums[0]]
        while i != pointer:
            s += pointer
            pointer = final[pointer]
        for c in s:
            nums.remove(c)
        if len(s) > 1:
            lst.append(s)
    if len(lst) == 0:
        lst = ["I"]
    return lst

#returns final dictionary mapping of permutation in simplest form
def simplify(perm):
    maps = [product(cycle) for cycle in perm]
    final = maps[-1]
    for i in xrange(len(maps)-1):
        for n in final:
            final[n] = maps[len(maps) - i - 2][final[n]]
    return final

#removes parentheses around input strings and splits accordingly
def preprocess(perm):
    if "(" and ")" not in perm:
        raise ValueError("Use '('' and ')' to denote cycle!")
    return [", ".join(cycle.split()) for cycle in re.split(r'[()]', perm) if cycle.strip()]

#prints out final result in cycle notation format with parentheses
def display(lst):
    s = ""
    for i in lst:
        s += "(" + i + ")"
    return s.strip()

def perm_mult(a = "(I)", b = "(I)"):
    map_a = simplify(preprocess(a))
    map_b = simplify(preprocess(b))
    
    a = path(map_a)
    b = path(map_b)
    
    a_inv = path(swap(map_a))
    b_inv = path(swap(map_b))
    
    ab = path(simplify(a+b))
    ba = path(simplify(b+a))
    
    aba_inv = path(simplify(a+b+a_inv))
    bab_inv = path(simplify(b+a+b_inv))
    print
    print "a =", display(a)
    print "b =", display(b)
    print "a^-1 =", display(a_inv)
    print "b^-1 =", display(b_inv)
    print "ab =", display(ab)
    print "ba =", display(ba)
    print "aba^-1 =", display(aba_inv)
    print "bab^-1 =", display(bab_inv)
    
    return ""

if __name__ == "__main__":
    p1 = raw_input("a: ")
    p2 = raw_input("b: ")
    perm_mult(p1, p2)