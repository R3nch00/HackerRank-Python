import numpy
n=int(input())
A=numpy.array([input().split() for _ in range(n)],float)
numpy.set_printoptions(legacy='1.13')
print (numpy.linalg.det(A))
