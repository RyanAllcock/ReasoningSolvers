from z3 import *
import time
s = Solver()
n = 3

# variables
withinRange = Function('withinRange', IntSort(), BoolSort())
i = Int('i')
s.add(ForAll([i], withinRange(i) == And(i >= 1, i <= n)))

# tiles
tile = Function('tile', IntSort(), IntSort(), IntSort())
x = Int('x')
y = Int('y')
s.add(ForAll([x,y], withinRange(tile(x,y))))

# value uniqueness
x1 = Int('x1')
x2 = Int('x2')
y1 = Int('y1')
y2 = Int('y2')
s.add(ForAll(y, ForAll([x1,x2], Implies(And(x1 != x2, withinRange(x1), withinRange(x2), withinRange(y)), tile(x1,y) != tile(x2,y)))))
s.add(ForAll(x, ForAll([y1,y2], Implies(And(y1 != y2, withinRange(x), withinRange(y1), withinRange(y2)), tile(x,y1) != tile(x,y2)))))

# scenario
s.add(tile(3,1) == 1)
s.add(tile(1,2) == 2)
#s.add(tile(3,3) == 3)

# outcome
tstart = time.time()
outcome = s.check()
tend = time.time()
print('time taken: {}'.format(float(tend - tstart)))
print(outcome)
if(outcome == sat):
	for j in range(1, n + 1):
		for i in range(1, n + 1):
			print(s.model().eval(tile(i,j)), end = '')
		print()





















#position in each row and column with same value
#x1 = Int('x1')
#x2 = Int('x2')
#y1 = Int('y1')
#y2 = Int('y2')
#s.add(ForAll([x1,x2,y],Implies(And(x1!=x2,withinRange(x1),withinRange(x2),withinRange(y)),(position(y,x1)!=position(y,x2)))))
#s.add(ForAll([x,y1,y2],Implies(And(y1!=y2,withinRange(y1),withinRange(y2),withinRange(x)),(position(y1,x)!=position(y2,x)))))