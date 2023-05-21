# A valid mobile number is a ten digit number starting with a 7,8 or 9.

import re
for _ in range(int(input())):
    print('YES') if re.match(r'[789]\d{9}$',input()) else  print('NO')