students = {}
my_students = {}


def score():
    while True:
        line = input()
        if line == '#':
            break
        student = line.split()
        student[1] = int(student[1])
        if student[0] not in students:
            students[student[0]] = [student[1]]
        else:
            students[student[0]].append(student[1])

    for x in students:
        L = len(students[x])
        sum_my = 0
        for s in students[x]:
            sum_my += s
        average = sum_my / L
        my_students[x] = average
score()
print("姓 名     平均成绩")
for x in my_students:
    print(f"{x:<9}{my_students[x]:.2f}")