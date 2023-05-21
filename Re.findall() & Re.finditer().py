import re
s = input()

vowels = '[AEIOUaeiou]{2,}'
consonant = '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
testpattern=re.compile(rf'(?<={consonant}){vowels}(?={consonant})')

result=testpattern.findall(s)
print(*result if len(result)>0 else [-1],sep='\n')