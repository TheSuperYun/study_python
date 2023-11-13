list_my = input().split(' ')
number_my = {}
for x in list_my:
    if x not in number_my:
        number_my[x] = 1
    else:
        number_my[x] +=1
print(number_my)