year = eval(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
