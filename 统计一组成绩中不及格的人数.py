n = eval(input())
sum = 0.0
count = 0
for x in range(n):
    temp = eval(input())
    sum += temp
    if temp < 60:
        count += 1
print(f"平均分为：{sum/n:.2f},有{count}个学生不及格。")