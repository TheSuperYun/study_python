students = {}
while True:
    line = input()
    if line == '#':
        break
    name, score = line.split()
    score = float(score)

    # 将成绩添加到学生的成绩列表中
    if name in students:
        students[name].append(score)
    else:
        students[name] = [score]
averages = {}
for name,score in students.items():
    average = sum(score)/len(score)
    averages[name] = average
print("姓 名     平均成绩")
for name,score in averages.items():
    print(f"{name:<8} {score:.2f}")
