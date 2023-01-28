events = input().split("|")
energy = 100
coins = 100
not_closed = True

for i in events:
    event = i.split("-")
    if event[0] == "rest":
        current_energy = int(event[1])
        if energy + current_energy > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += current_energy
            print(f"You gained {current_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            current_coins = int(event[1])
            coins += int(event[1])
            print(f"You earned {current_coins} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= int(event[1]):
            coins -= int(event[1])
            print(f"You bought {event[0]}.")
        else:
            not_closed = False
            print(f"Closed! Cannot afford {event[0]}.")
            break

if not_closed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")