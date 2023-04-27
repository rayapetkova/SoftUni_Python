from collections import deque


def check_valid_indices(c_row, c_col):
    return 0 <= c_row < SIZE and 0 <= c_col < SIZE


def find_squirrel(curr_matrix):
    for c_row in range(SIZE):
        for c_col in range(SIZE):
            pos = curr_matrix[c_row][c_col]
            if pos == "s":
                return c_row, c_col


SIZE = int(input())
directions = deque(input().split(", "))
matrix = [list(input()) for i in range(SIZE)]

moves_dict = {
    'left': (0, -1),
    'right': (0, +1),
    'down': (+1, 0),
    'up': (-1, 0)
}

squirrel = find_squirrel(matrix)
break_flag = False
total_hazelnuts = 0

while directions:
    direction = directions.popleft()
    row, col = squirrel[0] + moves_dict[direction][0], squirrel[1] + moves_dict[direction][1]
    if not check_valid_indices(row, col):
        print(f"The squirrel is out of the field.")
        break_flag = True
        break
    if matrix[row][col] == 'h':
        total_hazelnuts += 1
        if total_hazelnuts == 3:
            print(f"Good job! You have collected all hazelnuts!")
            break_flag = True
            break
        matrix[row][col] = "*"
        squirrel = (row, col)
        continue
    elif matrix[row][col] == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...")
        break_flag = True
        break
    squirrel = (row, col)

if not break_flag and total_hazelnuts < 3:
    print(f"There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {total_hazelnuts}")