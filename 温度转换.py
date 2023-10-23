arr = input()
num = eval(arr[:-1])
if arr[-1] == "C":
    tem = num * 1.8 + 32
    print(f"{tem}F")
elif arr[-1] == "F":
    tem = (num - 32) / 1.8
    print(f"{tem}C")
