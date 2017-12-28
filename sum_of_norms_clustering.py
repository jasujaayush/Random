import random
import numpy as np
import cvxpy

def getRandomPointsInCircle(Cx, Cy, radius, number):
	points = []
	while len(points) < number:
		x = random.uniform(Cx-radius, Cx+radius)
		y = random.uniform(Cy-radius, Cy+radius)
		distance = ((Cx - x)**2 + (Cy - y)**2)**0.5
		if distance < radius and [x,y] not in points:
			points.append([x,y])
	return points

d=2
n = 10
p1 = np.array(getRandomPointsInCircle(10,10,0.5,n)).T
p2 = np.array(getRandomPointsInCircle(-10,-10,0.5,n)).T
p = np.hstack((p1, p2))

i = 0
N = 2*n
Q = np.zeros((N*N, N))
for t in range(N):
	for k in range(t+1, N):
		Q[i,t] = 1
		Q[i,k] = -1
		i += 1

## son clustering
reg_param =0.001;
#cvx_begin quiet
X = cvxpy.Variable(d,N) #variables X(n,N)
#minimize( sum(sum((x-X).*(x-X)))+lambda*sum(norms(J*X',2,2)) )
prob = cvxpy.Minimize( cvxpy.sum_entries( cvxpy.square((p-X))) + reg_param*cvxpy.sum_entries(cvxpy.norm(Q*(X.T),2,1 )) )	
prob = cvxpy.Problem(prob)
prob.solve

eps = 0.1
clusters = 1
m = 1
mapping = np.zeros((1,N))
for i in range(N):
	if mapping[0,i] == 0:
		mapping[0,i] = m
		for j in range(i+1,N):
			d = cvxpy.sum_entries(cvxpy.square(X[:,i] - X[:,j]))
			if d.value**0.5 < eps:
				mapping[0,j] = m
		m += 1			

