import re
flaot_regex=re.compile("[+-]?[0-9]*\.[0-9]+")

def float_check(s):
    if flaot_regex.fullmatch(s):
        return True
    else:
        return False
i=int(input())
for i in range(i):
    print(float_check(input()))