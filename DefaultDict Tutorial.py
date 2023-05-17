"""
Ternary Operator: 
[on_true] if [expression] else [on_false] 

"""

from collections import defaultdict
input_n,input_m=map(int,input().split())
d=defaultdict(list)
for i in range(input_n):
    ans1=input()
    d[ans1].append(i+1)
for j in range(input_m):
    ans2=input()
    print(*d[ans2]) if ans2 in d else print(-1)