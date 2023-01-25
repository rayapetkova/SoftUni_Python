days = int(input())
hours = int(input())

total = 0

for i in range(1, days + 1):
    total_first = 0
    total_second = 0
    total_third = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            total_first = total_first + 2.50
        elif i % 2 != 0 and j % 2 == 0:
            total_second = total_second + 1.25
        else:
            total_third = total_third + 1
    total_sum = total_first + total_second + total_third
    print(f"Day: {i} - {total_sum:.2f} leva")
    total = total + total_sum
print(f"Total: {total:.2f} leva")