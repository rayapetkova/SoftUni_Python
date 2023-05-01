SIZE = 6
matrix = [input().split() for i in range(SIZE)]
pos = list(input())
my_position = (int(pos[1]), int(pos[4]))

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

while True:
    line = input()
    if line == "Stop":
        break
    command = line.split(", ")
    direction = command[1]
    row, col = my_position[0] + directions[direction][0], my_position[1] + directions[direction][1]
    if "Create" in command:
        value = command[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value
    elif "Update" in command:
        value = command[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value
    elif "Delete" in command:
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    elif "Read" in command:
        if matrix[row][col] != ".":
            print(matrix[row][col])
    my_position = (row, col)

[print(' '.join(nested)) for nested in matrix]
