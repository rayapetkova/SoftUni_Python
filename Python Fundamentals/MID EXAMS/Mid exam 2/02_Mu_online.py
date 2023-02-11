rooms = input().split("|")

health = 100
bitcoins = 0

for i in rooms:
    command = i.split()
    number = int(command[1])
    if "potion" in command:
        if health + number > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
        else:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
    elif "chest" in command:
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {rooms.index(i) + 1}")
            exit()

if health >= 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")