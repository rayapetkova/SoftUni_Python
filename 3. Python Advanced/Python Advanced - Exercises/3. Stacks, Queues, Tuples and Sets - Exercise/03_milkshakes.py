from collections import deque

chocolates = [int(el) for el in input().split(", ")]
cups_of_milk = deque([int(el) for el in input().split(", ")])

milkshakes = 0
while chocolates and cups_of_milk:
    last_chocolate, first_cup_of_milk = chocolates[-1], cups_of_milk.popleft()
    if last_chocolate <= 0 and first_cup_of_milk <= 0:
        chocolates.pop()
        continue

    if last_chocolate <= 0:
        chocolates.pop()
        cups_of_milk.appendleft(first_cup_of_milk)
        continue

    if first_cup_of_milk <= 0:
        continue

    if last_chocolate == first_cup_of_milk:
        chocolates.pop()
        milkshakes += 1
    else:
        cups_of_milk.append(first_cup_of_milk)
        chocolates[-1] -= 5

    if milkshakes == 5:
        break

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(chocolate) for chocolate in chocolates)}")
else:
    print(f"Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(cup) for cup in cups_of_milk)}")
else:
    print(f"Milk: empty")
