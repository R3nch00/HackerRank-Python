"""

Formula used ->
Average = Sum of Distinct Heights/Total Number of Distinct Heights

"""

def average(array): #Avergae function created which'll take input(Array)
    a=set(array) #Converted array into set
    avg=sum(a)/len(a)
    return(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)