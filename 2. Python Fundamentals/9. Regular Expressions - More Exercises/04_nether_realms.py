import re

names = input().split(",")
stored_names = {}

health_pattern = r"[^+\-\*\/\.]"
damage_pattern = r"-?(0|[1-9]\d*)(\.\d*)?"
multiply_and_divide_pattern = r"[\*\/]"

for name in names:
    name = name.strip()
    stored_names[name] = {'health': 0, 'damage': 0}
    total_health = 0
    symbols_health = re.findall(health_pattern, name)
    symbols_health = [x for x in symbols_health if not x.isdigit()]
    for symbol in symbols_health:
        total_health += ord(symbol)
    stored_names[name]['health'] = total_health
    numbers_damage = re.finditer(damage_pattern, name)
    numbers = []
    for valid in numbers_damage:
        numbers.append(float(valid.group()))
    sum_damage = sum(numbers)
    symbols_multiply_divide = re.findall(multiply_and_divide_pattern, name)
    for current in symbols_multiply_divide:
        if current == "*":
            sum_damage *= 2
        else:
            sum_damage /= 2
    stored_names[name]['damage'] = sum_damage

for key, value in sorted(stored_names.items(), key=lambda x: x[0]):
    print(f"{key} - {value['health']} health, {value['damage']:.2f} damage")