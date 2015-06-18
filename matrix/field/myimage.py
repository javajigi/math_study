from image import *
from math import *
from plotting import plot

def rotate(z, r):
	return z * e ** (r * 1j)

pts = file2image("img01.png")
graiedPts = color2gray(pts)

s = set()
rowLen = len(graiedPts)
colLen = len(graiedPts[0])

for row in range(0, len(graiedPts)):
	for column in range(0, len(graiedPts[row])):
		if (graiedPts[row][column] < 128):
			s.add(complex(row, column))

# move = complex(189, 189)
result = {z * -1j + complex(0, 189) for z in s}
plot({rotate(z, pi/4)/2 for z in result}, 189)