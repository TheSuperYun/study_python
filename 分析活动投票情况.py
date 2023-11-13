number_my = [6, 7, 8, 9, 10]
list_my = input().split(",")
list_me = []
list_end = []
i = 0
for x in list_my:
    list_me.append(int(x))
    i += 1
for x in number_my:
    if x not in list_me:
        list_end.append(x)
n = 0
for x in list_end:
    if n == len(list_end) - 1:
        print(x, end="")
    else:
        print(x, end=' ')
    n += 1
