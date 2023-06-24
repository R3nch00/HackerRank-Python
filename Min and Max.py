import numpy
n,m=map(int,input().split())
lista=[list(map(int,input().split())) for i in range(n)]
a=numpy.array(lista)
print(max(numpy.min(a,axis=1)))