pirate_ship = [int(i) for i in input().split(">")]
war_ship = [int(i) for i in input().split(">")]
maximum_health = int(input())
lost = False

while True:
    line = input()
    if line == "Retire":
        if not lost:
            print(f"Pirate ship status: {sum(pirate_ship)}")
            print(f"Warship status: {sum(war_ship)}")
        break
    command = line.split()
    if "Fire" in command:
        idx = int(command[1])
        damage = int(command[2])
        if 0 <= idx < len(war_ship):
            war_ship[idx] -= damage
            if war_ship[idx] <= 0:
                print(f"You won! The enemy ship has sunken.")
                lost = True
                break

    elif "Defend" in command:
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx < len(pirate_ship) and 0 < end_idx < len(pirate_ship):
            for i in range(start_idx, end_idx + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    lost = True
                    break

    elif "Repair" in command:
        idx = int(command[1])
        health = int(command[2])
        if 0 <= idx < len(pirate_ship):
            pirate_ship[idx] = min(maximum_health, pirate_ship[idx] + health)

    elif "Status" in command:
        low_sections = (20 / 100) * maximum_health
        count = [+1 for i in pirate_ship if i < low_sections]
        print(f"{sum(count)} sections need repair.")