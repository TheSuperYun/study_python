list_my = input()
flag = 1
for x in list_my:
    if not (49 <= ord(x) <= 57 or 97 <= ord(x) <= 122):
        flag = 0
if flag == 1:
    print("全是数字和小写字母")
elif flag == 0:
    print("不全是数字和小写字母")
