import math

y = 0
x = eval(input())
if x < 1:
    y = math.log2(math.fabs(x))
elif x < 10:
    y = math.e ** x
else:
    y = 3 * math.sqrt(x / 3) + 10
print(f"{y:.2f}")