x = eval(input())  # 1035=1+2+...+45
i = 1
s = 0
while s < x:
    s += i
    i += 1
if s > 3:
    print(f"{s}=1+2+...+{i-1}")
elif s==1:
    print(f"{s}=1")
elif s==2:
    print(f"{s}=1+2")
elif s==3:
    print(f"{s}=1+2")
elif 3<s<6:
    print(f"{s}=1+2+3")