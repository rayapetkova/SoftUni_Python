event = input().split("|")
all_gained_energy = 100
all_coins = 100
finished_day = True
exceeded = False
exceeded_energy = 0

for i in event:
    gained_energy = 0
    coins = 0
    price_ingredient = 0
    if "rest" in i:
        i = i.split("-")
        all_gained_energy += int(i[1])
        if all_gained_energy <= 100:
            gained_energy = int(i[1])
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {all_gained_energy}.")
        else:
            exceeded = True
            exceeded_energy += int(i[1])
            all_gained_energy -= int(i[1])
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {all_gained_energy}.")
    elif "order" in i:
        i = i.split("-")
        coins = int(i[1])
        all_gained_energy -= 30
        if all_gained_energy >= 0:
            all_coins += int(i[1])
            print(f"You earned {coins} coins.")
        else:
            all_gained_energy += 50
            print(f"You had to rest!")
    else:
        i = i.split("-")
        price_ingredient = int(i[1])
        if all_coins >= price_ingredient:
            all_coins -= price_ingredient
            print(f"You bought {i[0]}.")
        else:
            finished_day = False
            print(f"Closed! Cannot afford {i[0]}.")
            break

if finished_day:
    print(f"Day completed!\nCoins: {all_coins}\nEnergy: {all_gained_energy}")