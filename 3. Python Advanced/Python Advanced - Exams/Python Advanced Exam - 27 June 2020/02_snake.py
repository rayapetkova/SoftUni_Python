def check_valid_indices(r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())
matrix = []
snake = ()
burrows = []

for i in range(size):
    line = input()

    if "S" in line:
        snake = (i, line.index("S"))
    if "B" in line:
        burrows.append((i, line.index("B")))

    matrix.append(list(line))

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

matrix[snake[0]][snake[1]] = "."
food_quantity = 0

while food_quantity < 10:
    direction = input()

    row, col = snake[0] + directions[direction][0], snake[1] + directions[direction][1]

    if not check_valid_indices(row, col):
        print(f"Game over!")
        break

    if matrix[row][col] == "*":
        food_quantity += 1
    elif (row, col) in burrows:
        burrows.remove((row, col))
        matrix[row][col] = "."
        row, col = burrows[0][0], burrows[0][1]

    snake = (row, col)
    matrix[row][col] = "."

if food_quantity >= 10:
    print(f"You won! You fed the snake.")
    matrix[snake[0]][snake[1]] = "S"

print(f"Food eaten: {food_quantity}")
[print(''.join(nested)) for nested in matrix]
