weight = float(input())
height = float(input())
BMI = weight * 703 / height ** 2

if BMI < 18.5:
    print(f"BMI = {int(BMI * 100) / 100}")
    print("体重过轻")
elif BMI <= 25:
    print(f"BMI = {int(BMI * 100) / 100}")
    print("体重最佳")
else:
    print(f"BMI = {int(BMI * 100) / 100}")
    print("体重超重")
