# interest=money×(1+rate) year −money
import math

arr = input()
date = arr.split("-")  # 2009-5-12
for x in range(0, 3):
    date[x] = int(date[x])
lest = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def month(date):
    if (date[0] % 400 == 0) or (date[0] % 4 == 0 and date[0] % 100 != 0):
        lest[1] = 29
        if date[2] + 1 > lest[date[1] - 1]:
            if date[1] == 12:
                date[1] = 1
                date[0] += 1
                date[2] = 1
            else:
                date[1] += 1
                date[2] = 1
        else:
            date[2] += 1
    else:
        lest[1] = 28
        if date[2] + 1 > lest[date[1] - 1]:
            if date[1] == 12:
                date[1] = 1
                date[0] += 1
                date[2] = 1
            else:
                date[1] += 1
                date[2] = 1
        else:
            date[2] += 1


month(date)
print(f"{date[0]}-{date[1]}-{date[2]}")
