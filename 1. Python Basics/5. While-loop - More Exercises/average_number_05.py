n = int(input())

sum_nums = 0

for i in range(1, n + 1):
    num = float(input())
    sum_nums = sum_nums + num

average = sum_nums / n
print(f"{average:.2f}")