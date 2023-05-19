from itertools import combinations
word,length=input().split()
for i in range(1, int(length)+1): #Created for loop in the range of 1 to (length+1)
    for j in combinations(sorted(word), i):
         print (''.join(j))