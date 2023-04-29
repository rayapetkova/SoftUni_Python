def find_submarine(curr_matrix):
    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "S":
                return r, c


SIZE = int(input())
matrix = [list(input()) for i in range(SIZE)]

submarine = find_submarine(matrix)
matrix[submarine[0]][submarine[1]] = "-"

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

mines, battle_cruisers = 0, 0
while True:
    direction = input()
    row, col = submarine[0] + directions[direction][0], submarine[1] + directions[direction][1]
    if matrix[row][col] == "*":
        mines += 1
        matrix[row][col] = "-"
        if mines >= 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            matrix[row][col] = "S"
            break
    if matrix[row][col] == "C":
        battle_cruisers += 1
        matrix[row][col] = "-"
        if battle_cruisers == 3:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            matrix[row][col] = "S"
            break
    submarine = row, col


[print(''.join(nested)) for nested in matrix]