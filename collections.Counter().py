from collections import Counter
x=int(input()) # Input of x,the total num of shoes
y=Counter(map(int,input().split())) # Input of y,the list of all shoe sizes & arrange them as a dictionary
z=int(input()) #  Input of z,the total number of customers

total=0

for i in range(z): # Size taken as inut & verify if the input size is in y
    size, rate=map(int, input().split())
    if y[size]: 
        y[size]-=1
        total+=rate
print(total) # All the rates in total & print it