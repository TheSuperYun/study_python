n = eval(input())


def CommonDivisor(x, y):
    if x == y:
        return x
    if x > y:
        while x % y != 0:
            tem = x % y
            x = y
            y = tem
        return y
    if x < y:
        while y % x != 0:
            tem = y % x
            y = x
            x = tem
        return x


for x in range(n):
    list = input().split()
    a = int(list[0])
    b = int(list[1])
    common = CommonDivisor(a, b)
    print(common)
