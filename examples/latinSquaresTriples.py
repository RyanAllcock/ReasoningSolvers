from z3 import *
import time
s = Solver()

# scenario
n = 3
V = [(3,1,1), (1,2,2), (3,3,3)]

# matrix elements
M = []
for j in range(n):
	row = []
	for i in range(n):
		id = Int('M_' + str(i) + ',' + str(j))
		s.add(id >= 1)
		s.add(id <= n)
		row.append(id)
	M.append(row)

# rows
for k in range(n):
	for i in range(k):
		for j in range(n):
			s.add(M[j][i] != M[j][k])
			
# columns
for k in range(n):
	for j in range(k):
		for i in range(n):
			s.add(M[j][i] != M[k][i])

# known values
for (i,j,v) in V:
	s.add(M[j-1][i-1] == v)

# outcome
tstart = time.time()
outcome = s.check()
tend = time.time()
print('time taken: {}'.format(float(tend - tstart)))
print(outcome)
if(outcome == sat):
	for j in range(n):
		for i in range(n):
			print(s.model().eval(M[j][i]), end = ' ')
		print()