list_price = input().split()
ton = int(list_price[0])
km = int(list_price[1])
price = 1
fee = 0
if km < 250:
    price = 1
elif km < 500:
    price *= 0.98
elif km < 1000:
    price *= 0.95
elif km < 2000:
    price *= 0.92
elif km < 3000:
    price *= 0.9
else:
    price *= 0.85
fee = km * price * ton
print(fee)
