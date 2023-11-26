def lcm(a, b):
    if a > b:
        a1 = a
        b1 = b
        while a % b != 0:
            temp = a % b
            a = b
            b = temp
        return (a1//b)*(b1//b)*b

    else:
        a1 = a
        b1 = b
        while b % a != 0:
            temp = b % a
            b = a
            a = temp
        return (b1//a)*(a1//a)*a


a = eval(input())
b = eval(input())#6和9的最小公倍数为18
num = lcm(a,b)
print(f"{a}和{b}的最小公倍数为{num}")
