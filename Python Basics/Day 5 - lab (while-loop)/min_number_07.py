import sys

min_number = sys.maxsize

while True:
    number = input()

    if number == "Stop":
        break
    number = float(number)

    if number < min_number:
        min_number = number
print(f"{min_number:.0f}")