list_my = input().split(",")
list_count = []
for x in list_my:
    list_count.append(int(x))
count = len(list_count)
i = 0
for x in list_count:
    if x >= 85:
        i += 1
print(f"优秀率为{(i/count)*100:.2f}%。")