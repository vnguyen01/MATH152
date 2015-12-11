from itertools import combinations, product

#nxn matrix
n = 2

#field order
q = 5

#elements in \ZZ_5
elements = [-2, -1, 0, 1, 2]
basis = [c for c in combinations(elements, n**n)]

#matrix elements in SL(2, \ZZ_5)
matrices = []
for b in basis:
	for p in product(b, repeat=n**n):
		#det(p) = 1 for SL
		if (p[0]*p[3]-p[1]*p[2])%5 == 1:
			matrices.append(p)

matrices = list(set(matrices))
assert((q**2 - 1)*(q**2 - q)/(q-1) == len(matrices))

#2-component vectors over \ZZ_5
line1 = [(1,0),(2,0),(-2,0),(-1,0)]
line2 = [(0,1),(0,2),(0,-2),(0,-1)]
line3 = [(1,1),(2,2),(-2,-2),(-1,-1)]
line4 = [(1,2),(2,-1),(-2,1),(-1,-2)]
line5 = [(1,-2),(2,1),(-2,-1),(-1,2)]
line6 = [(1,-1),(2,-2),(-2,2),(-1,1)]

#matrices that take line1 -> line4 and line2 -> line6
for m in matrices:
	if (m[0] * line1[0][0] + m[1] * line1[0][1], 
		m[2] * line1[0][0] + m[3] * line1[0][1]) in line4 and \
	   (m[0] * line2[0][0] + m[1] * line2[0][1], 
	   	m[2] * line2[0][0] + m[3] * line2[0][1]) in line6:
	   print m

