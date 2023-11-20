def rabbit(n):
    a2 = 1
    a1 = 0
    a = 0
    for x in range(n-1):
        x2 = a2
        x1 = a1
        x = a
        a2 = x+x1
        a1 = x2
        a += x1

    return a1+a2+a


try:
    n = int(input())
    print(rabbit(n))
except EOFError:
    print("输入结束，程序终止。")
