from plotting import plot

def add(v, w):
	return [v[0] + w[0], v[1] + w[1]]

def scalar_vector_mul(alpha, v):
	return [alpha * v[i] for i in range(len(v))]

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]

# plot([scalar_vector_mul(-0.5, v) for v in L], 4)

# v = [3, 2]
# plot([add(scalar_vector_mul(i/100.0, v), [0.5, 1]) for i in range(0, 101)], 5)

u = [2, 3]
v = [5, 7]

plot([scalar_vector_mul(i/100.0, u) for i in range(0, 101)], 5)
plot([scalar_vector_mul(i/100.0, v) for i in range(0, 101)], 10)