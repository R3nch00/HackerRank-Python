from itertools import product # Imported  product from Itertools

input_A = list(map(int, input().split()))
input_B = list(map(int, input().split()))

print(*list(product(input_A, input_B))) # Converted output into a list and printed