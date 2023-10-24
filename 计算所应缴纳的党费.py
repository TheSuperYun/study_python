income = eval(input())
tax = 1
if income <= 400:
    tax = 0.005
elif income <= 600:
    tax = 0.01
elif income <= 800:
    tax = 0.015
elif income <= 1500:
    tax = 0.02
else:
    tax = 0.03
fee = income*tax
print(f"交纳党费={fee:.1f}")