import re

pattern = r"^%(?P<name>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^|$%.\d]*(?P<price>\d+\.?\d*)\$$"
total = 0

while True:
    info = input()
    if info == "end of shift":
        break
    valid_info = re.finditer(pattern, info)
    for valid in valid_info:
        price = float(valid['count']) * float(valid['price'])
        total += price
        print(f"{valid['name']}: {valid['product']} - {price:.2f}")

print(f"Total income: {total:.2f}")