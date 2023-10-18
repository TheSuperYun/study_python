arr = input()
date = arr.split("-")
for x in range(0, 3):
    date[x] = int(date[x])
print(date)
