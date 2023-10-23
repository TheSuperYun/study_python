arr = input().split(",")
exper = int(arr[0])
exam = int(arr[1])
if (exper < 60) or (exam < 60):
    print("不合格")
elif (exper + exam) / 2 >= 90:
    print("成绩优秀")
elif (exper + exam) / 2 >= 80:
    print("良好")
else:
    print("通过")
