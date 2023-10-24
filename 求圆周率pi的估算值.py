import math

n = eval(input())
sum = 0


def add(n1):
    if n1 % 2 == 1:
        return -(1 / ((2 * n1 + 1) * 3 ** n1))
    else:
        return 1 / ((2 * n1 + 1) * 3 ** n1)


for x in range(1, n + 1):
    sum += add(x)
sum = math.sqrt(12) * (1 + sum)
print(f"pi = {sum}")

