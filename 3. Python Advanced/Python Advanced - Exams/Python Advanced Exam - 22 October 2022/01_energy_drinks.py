from collections import deque

caffeine = [int(n) for n in input().split(", ")]
energy_drinks = deque(int(n) for n in input().split(", "))
initial = 0

while caffeine and energy_drinks:
    last_milligrams, drink = caffeine.pop(), energy_drinks.popleft()
    result = last_milligrams * drink
    if result + initial <= 300:
        initial += result
    else:
        energy_drinks.append(drink)
        if initial - 30 >= 0:
            initial -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(n) for n in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial} mg caffeine.")