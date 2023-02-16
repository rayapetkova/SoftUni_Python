days = int(input())
daily_plunder = int(input())
expected = float(input())

total = 0

for i in range(1, days + 1):
    total += daily_plunder
    if i % 3 == 0:
        additional = (50 / 100) * daily_plunder
        total += additional
    if i % 5 == 0:
        lost = (30 / 100) * total
        total -= lost

if total >= expected:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = (total / expected) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")