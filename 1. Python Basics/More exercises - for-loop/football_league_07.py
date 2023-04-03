stadium_seats = int(input())
fans = int(input())

counter = 0
percents_a = 0
percents_b = 0
percents_v = 0
percents_g = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

for i in range(1, fans + 1):
    sector = input()
    if sector == "A":
        counter1 = counter1 + 1
        percents_a = (counter1 / fans) * 100
    elif sector == "B":
        counter2 = counter2 + 1
        percents_b = (counter2 / fans) * 100
    elif sector == "V":
        counter3 = counter3 + 1
        percents_v = (counter3 / fans) * 100
    elif sector == "G":
        counter4 = counter4 + 1
        percents_g = (counter4 / fans) * 100

print(f"{percents_a:.2f}%")
print(f"{percents_b:.2f}%")
print(f"{percents_v:.2f}%")
print(f"{percents_g:.2f}%")

percents_fans = (fans / stadium_seats) * 100
print(f"{percents_fans:.2f}%")