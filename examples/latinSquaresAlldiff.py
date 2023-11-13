from ortools.sat.python import cp_model
import time

# scenario
n = 6
V = []

# model
model = cp_model.CpModel()

# variables
M = []
for j in range(n):
	t = []
	for i in range(n):
		t.append(model.NewIntVar(1, n,  'M_' + str(i) + ',' + str(j)))
	M.append(t)

# rows
for j in range(n):
	model.AddAllDifferent(M[j])

# columns
for i in range(n):
	model.AddAllDifferent([M[j][i] for j in range(n)])

# known values
for (i,j,v) in V:
	model.Add(M[j-1][i-1] == v)

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
			print(solver.Value(M[j][i]), end = ' ')
		print("")
else:
	print('unsat')