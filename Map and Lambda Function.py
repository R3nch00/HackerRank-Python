cube=lambda x: x**3
sqrt=lambda x: x**0.5

def fibonacci(n):
    phi=(1+sqrt(5))/2
    return [int((phi**i-(1 -phi)**i)/ sqrt(5)) for i in range(n)]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))