from collections import OrderedDict
o=OrderedDict()
input_=int(input())
for _ in range(input_):
    item,space,price=input().rpartition(' ') #rpartition method to split our inputs in three parts
    o[item]=o.get(item,0)+int(price)
for item,price in o.items():
    print(item,price)