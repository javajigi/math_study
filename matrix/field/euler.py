from math import *
from plotting import plot

def w(n):
	return e ** (2 * pi * 1j / n)

def rotate(z, r):
	return z * e ** (r * 1j)

a = {rotate(w(n), pi/4) for n in range(1, 20)}

plot(a, 4)