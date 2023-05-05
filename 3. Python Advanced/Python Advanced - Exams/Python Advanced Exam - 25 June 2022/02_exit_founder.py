def index_increase(curr_idx):
    curr_idx += 1
    if curr_idx == 2:
        curr_idx = 0
    return curr_idx


names = input().split(", ")
SIZE, matrix = 6, []
tom, jerry = (), ()

for r in range(SIZE):
    line = input().split()
    matrix.append(line)

idx = 0
tom_wall, jerry_wall = False, False
while True:
    coordinates = list(input())
    row, col = int(coordinates[1]), int(coordinates[4])
    if tom_wall and idx == names.index("Tom"):
        idx = index_increase(idx)
        tom_wall = False
        continue
    if jerry_wall and idx == names.index("Jerry"):
        idx = index_increase(idx)
        jerry_wall = False
        continue
    if matrix[row][col] == "E":
        if idx == names.index("Tom"):
            player = "Tom"
        else:
            player = "Jerry"
        print(f"{player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        if idx == names.index("Tom"):
            player, winner = "Tom", "Jerry"
        else:
            player, winner = "Jerry", "Tom"
        print(f"{player} is out of the game! The winner is {winner}.")
        break
    elif matrix[row][col] == "W":
        if idx == names.index("Tom"):
            tom_wall, player = True, "Tom"
        else:
            jerry_wall, player = True, "Jerry"
        print(f"{player} hits a wall and needs to rest.")
    idx = index_increase(idx)
