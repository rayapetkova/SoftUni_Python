days = int(input())
hours = int(input())

all_sum = 0

for day in range(1, days + 1):
    total = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total = total + 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            total = total + 1.25
        else:
            total = total + 1
    print(f"Day: {day} - {total:.2f} leva")
    all_sum = all_sum + total

print(f"Total: {all_sum:.2f} leva")
