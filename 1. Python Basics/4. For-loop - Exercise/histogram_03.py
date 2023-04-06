n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for num in range(1, n + 1):
    number = int(input())
    if number < 200:
        p1 = p1 + 1
    elif 200 <= number < 400:
        p2 = p2 + 1
    elif 400 <= number < 600:
        p3 = p3 + 1
    elif 600 <= number < 800:
        p4 = p4 + 1
    elif number >= 800:
        p5 = p5 + 1

percents_p1 = (p1 / n) * 100
print(f"{percents_p1:.2f}%")

percents_p2 = (p2 / n) * 100
print(f"{percents_p2:.2f}%")

percents_p3 = (p3 / n) * 100
print(f"{percents_p3:.2f}%")

percents_p4 = (p4 / n) * 100
print(f"{percents_p4:.2f}%")

percents_p5 = (p5 / n) * 100
print(f"{percents_p5:.2f}%")