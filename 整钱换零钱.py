z = 0
for i in range(1, 51):
    for j in range(1, 11):
        for k in range(1, 6):
            for l in range(1, 3):
                if i + 5 * j + 10 * k + 20 * l == 50:
                    print(f"可换得1元{i}张，5元{j}张，10元{k}张，20元{l}张。")
                    z+=1

print(f"共{z}种方案。")
