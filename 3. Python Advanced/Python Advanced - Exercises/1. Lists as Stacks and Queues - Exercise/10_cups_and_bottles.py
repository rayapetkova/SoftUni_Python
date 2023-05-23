from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = list(map(int, input().split()))
wasted_water = 0

while True:
    if not cups:
        print(f"Bottles: {' '.join(str(some_bottle) for some_bottle in bottles)}")
        break

    elif not bottles:
        print(f"Cups: {' '.join(str(some_cup) for some_cup in cups)}")
        break

    cup = cups.popleft()
    bottle = bottles.pop()

    if cup <= bottle:
        wasted_water += bottle - cup
    else:
        cups.appendleft(cup)
        cups[0] -= bottle

print(f"Wasted litters of water: {wasted_water}")