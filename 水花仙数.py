n = eval(input())
x = 10 ** (n - 1)
while x < 10 ** n:
    Sum = 0
    i = x
    while i:
        Rem = i % 10
        Sum += Rem ** n
        i //= 10
    if Sum == x:
        print(x)
    x += 1
