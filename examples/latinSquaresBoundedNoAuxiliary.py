from ortools.sat.python import cp_model
import time

# scenario
n = 6
m = 2
V = []

# Creates the model.
model = cp_model.CpModel()

# Creates the variables
M = []
for j in range(n): # values between 1 and n
	t = []
	for i in range(n):
		t.append(model.NewIntVar(1, n, 'M_' + str(i) + ',' + str(j)))
	M.append(t)

# rows
for j in range(n):
	model.AddAllDifferent(M[j])

# columns
for i in range(n):
	model.AddAllDifferent([M[j][i] for j in range(n)])

# known values
for(i,j,v) in V:
	model.Add(M[j-1][i-1] == v)

# bounded no auxiliary variables
for j1 in range(m):
	for i1 in range(m):
		for j2 in range(n-m,n):
			for i2 in range(n-m,n):
				model.Add(M[j1][i1] < M[j2][i2])

# solver
solver = cp_model.CpSolver()
tstart = time.time()
status = solver.Solve(model)
tend = time.time()
print('time taken: {}'.format(float(tend - tstart)))

# outcome
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
	print('sat')
	for j in range(n):
		for i in range(n):
			print(solver.Value(M[j][i]), end=" ")
		print("")
else:
	print('unsat')