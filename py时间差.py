line1 = input().split(" ")
hour1 = eval(line1[0])
minute1 = eval(line1[1])
line2 = input().split()
hour2 = eval(line2[0])
minute2 = eval(line2[1])
if hour2 > hour1:
    minute3 = ((60 - minute1) + minute2) % 60
    hour3 = ((60 - minute1) + minute2) // 60 + hour2 - hour1 - 1
elif hour2 == hour1:
    minute3 = minute2 - minute1
    hour3 = 0
print(f"{hour3} {minute3}")
