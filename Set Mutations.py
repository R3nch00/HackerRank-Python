"""

.update() or |= 
.intersection_update() or &=
.difference_update() or -=
.symmetric_difference_update() or ^=

"""

input()
a=set(map(int, input().split()))
for _ in range(int(input())):
    name,*_ =input().split()
    getattr(a,name)(set(map(int,input().split())))
print(sum(a))