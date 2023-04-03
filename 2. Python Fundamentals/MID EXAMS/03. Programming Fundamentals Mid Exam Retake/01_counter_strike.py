energy = int(input())
wins = 0

while True:
    line = input()
    if line == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break
    distance = int(line)
    if energy >= distance:
        energy -= distance
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    if wins % 3 == 0:
        energy += wins
