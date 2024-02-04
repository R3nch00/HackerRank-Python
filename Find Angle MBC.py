import math

ab = float(input())
bc = float(input())

ac = math.hypot(ab, bc)

angle_b_radian = math.acos(bc / ac)

angle_b_degree = round(math.degrees(angle_b_radian))

print(angle_b_degree, '\u00B0', sep='')