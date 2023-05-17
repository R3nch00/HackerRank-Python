M=int(input())
set_a=set(map(int,input().split()))
N=int(input())
set_b=set(map(int,input().split()))
M=(set_a.difference(set_b))
N=(set_b.difference(set_a))
ans=M.union(N)
for i in sorted(ans):
        print (i)