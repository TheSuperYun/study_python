n = eval(input())
list_my = []
i = 0
while i < n:
    list_my.append(eval(input()))
    i += 1
list_my.remove(max(list_my))
list_my.remove(min(list_my))
print(f"{sum(list_my) / len(list_my):.2f}")
