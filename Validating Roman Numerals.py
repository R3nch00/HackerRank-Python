digit='(V?[I]{0,3}|I[VX])'
ten='(L?[X]{0,3}|X[LC])'
hundred='(D?[C]{0,3}|C[DM])'
thousand='M{0,3}'
regex_pattern=r"%s%s%s%s$" %(thousand,hundred,ten,digit)
import re
print(str(bool(re.match(regex_pattern, input()))))