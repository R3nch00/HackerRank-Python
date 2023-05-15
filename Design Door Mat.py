n,m = map(int,input().split()) #Take input n,m
for i in range(n//2): # Print the first half
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
	
print('WELCOME'.center(m,'-')) # Center part

for i in reversed(range(n//2)): # Print the last part
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
