n = eval(input())
list_my = input().split(' ')
i=0
for x in list_my:
    list_my[i] = int(x)
    i+=1
max_my = max(list_my)
num = list_my.index(max_my)
print(f"{max_my} {num}")