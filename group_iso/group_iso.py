from itertools import combinations, product

#nxn matrix
n = 2

#field order
q = 5

#det
d = 1

#elements in \ZZ_5
elements = [-2, -1, 0, 1, 2]
basis = [c for c in combinations(elements, n**n)]

#matrix elements in SL(2, \ZZ_5)
matrices = []
for b in basis:
	for p in product(b, repeat=n**n):
		#det(p) = d for SL
		if (p[0]*p[3]-p[1]*p[2])%5 == d:
			matrices.append(p)

matrices = list(set(matrices))
assert((q**2 - 1)*(q**2 - q)/(q-1) == len(matrices))

#2-component vectors over \ZZ_5
line1 = [(1,0),(2,0),(-2,0),(-1,0)] #y = 0
line2 = [(0,1),(0,2),(0,-2),(0,-1)] #x = 0
line3 = [(1,1),(2,2),(-2,-2),(-1,-1)] #y = x
line4 = [(1,2),(2,-1),(-2,1),(-1,-2)] #y = 2x
line5 = [(1,-2),(2,1),(-2,-1),(-1,2)] #y = -2x
line6 = [(1,-1),(2,-2),(-2,2),(-1,1)] #y = -x

def line_perm(m_on_line, line_x):
	return True if m_on_line in line_x else False

#subgroup G \in SL(2, \ZZ_5) s.t. G \cong S_3, cosets
for m in matrices:

	#effect of m on different vector subspaces
	Mline1 = (m[0] * line1[0][0] + m[1] * line1[0][1], m[2] * line1[0][0] + m[3] * line1[0][1])
	Mline2 = (m[0] * line2[0][0] + m[1] * line2[0][1], m[2] * line2[0][0] + m[3] * line2[0][1])
	Mline3 = (m[0] * line3[0][0] + m[1] * line3[0][1], m[2] * line3[0][0] + m[3] * line3[0][1])
	Mline4 = (m[0] * line4[0][0] + m[1] * line4[0][1], m[2] * line4[0][0] + m[3] * line4[0][1])
	Mline5 = (m[0] * line5[0][0] + m[1] * line5[0][1], m[2] * line5[0][0] + m[3] * line5[0][1])
	Mline6 = (m[0] * line6[0][0] + m[1] * line6[0][1], m[2] * line6[0][0] + m[3] * line6[0][1])

	if Mline1 in line2 and Mline2 in line3 and Mline3 in line1:
		print "(123)", m

	if Mline1 in line3 and Mline3 in line2 and Mline2 in line1:
		print "(132)", m

	if Mline1 in line2 and Mline3 in line3 and Mline2 in line1:
		print "(12)(3)", m

	if Mline2 in line3 and Mline1 in line1 and Mline3 in line2:
		print "(1)(23)", m

	if Mline2 in line2 and Mline1 in line3 and Mline3 in line1:
		print "(2)(13)", m


