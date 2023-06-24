import numpy
A=numpy.array([int(chr) for chr in input() if chr!= " " ])
B=numpy.array( [int(chr) for chr in input() if chr!= " " ])

print(numpy.inner(A,B))
print(numpy.outer(A,B))