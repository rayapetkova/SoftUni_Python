from collections import deque

textiles = deque(int(n) for n in input().split())
medicaments = [int(n) for n in input().split()]

items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}

final = {}
while textiles and medicaments:
    textile, medicament = textiles.popleft(), medicaments.pop()
    total = textile + medicament
    if total in items.keys():
        final[items[total]] = final.get(items[total], 0) + 1
    elif total > 100:
        final[items[100]] = final.get(items[100], 0) + 1
        remaining_sum = total - 100
        medicaments[-1] += remaining_sum
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print(f"Textiles and medicaments are both empty.")
elif not textiles:
    print(f"Textiles are empty.")
elif not medicaments:
    print(f"Medicaments are empty.")

sorted_final = sorted(final.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_final:
    print(f"{key} - {value}")
if medicaments:
    print(f"Medicaments left: {', '.join(str(n) for n in reversed(medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(str(n) for n in textiles)}")