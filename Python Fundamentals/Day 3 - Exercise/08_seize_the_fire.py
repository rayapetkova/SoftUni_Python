fire_cells = input().split("#")
water = int(input())

total_fire = 0
current_values = []

for i in fire_cells:
    el = i.split(" = ")
    value = int(el[1])
    if "High" in el:
        if 81 <= value <= 125:
            if water < value:
                continue
            current_values.append(value)
            water -= value
            total_fire += value
    elif "Medium" in el:
        if 51 <= value <= 80:
            if water < value:
                continue
            current_values.append(value)
            water -= value
            total_fire += value
    elif "Low" in el:
        if 1 <= value <= 50:
            if water < value:
                continue
            current_values.append(value)
            water -= value
            total_fire += value

effort = (25 / 100) * total_fire

print(f"Cells:")
for i in current_values:
    print(f" - {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")