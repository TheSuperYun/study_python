list_my = input().split(',')
i = 0
for x in list_my:
    list_my[i] = int(x)
    i+=1
list_my.remove(max(list_my))
list_my.remove(min(list_my))
print(f"{sum(list_my)/len(list_my):.1f}")