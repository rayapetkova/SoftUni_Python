num = int(input())
bonus = 0

if num <= 100:
    bonus = 5
elif 100 < num < 1000:
    bonus = (20 / 100) * num
elif num > 1000:
    bonus = (10 / 100) * num

if num % 2 == 0:
    bonus = bonus + 1
elif num % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(num + bonus)
