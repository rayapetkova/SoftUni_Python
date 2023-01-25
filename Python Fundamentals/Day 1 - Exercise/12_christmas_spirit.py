quantity_decorations = int(input())
days = int(input())

total = 0
spirit = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity_decorations = quantity_decorations + 2
    if i % 2 == 0:
        total = total + (2 * quantity_decorations)
        spirit = spirit + 5
    if i % 3 == 0:
        total = total + (8 * quantity_decorations)
        spirit = spirit + 13
    if i % 5 == 0:
        total = total + (15 * quantity_decorations)
        spirit = spirit + 17
    if i % 3 == 0 and i % 5 == 0:
        spirit = spirit + 30

    if i % 10 == 0:
        spirit = spirit - 20
        total = total + 3 + 3 + 17

if days % 10 == 0:
    spirit = spirit - 30

print(f"Total cost: {total}")
print(f"Total spirit: {spirit}")