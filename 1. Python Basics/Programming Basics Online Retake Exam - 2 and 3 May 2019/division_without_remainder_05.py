num = int(input())
counter_2 = 0
counter_3 = 0
counter_4 = 0

for i in range(1, num + 1):
    number = int(input())

    if number % 2 == 0:
        counter_2 = counter_2 + 1
    if number % 3 == 0:
        counter_3 = counter_3 + 1
    if number % 4 == 0:
        counter_4 = counter_4 + 1

percents_1 = (counter_2 / num) * 100
percents_2 = (counter_3 / num) * 100
percents_3 = (counter_4 / num) * 100

print(f"{percents_1:.2f}%")
print(f"{percents_2:.2f}%")
print(f"{percents_3:.2f}%")