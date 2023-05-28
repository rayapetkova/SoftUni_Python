size = int(input())
bomb_field = [[int(x) for x in input().split()] for _ in range(size)]
bombs = [tuple([int(x) for x in bomb.split(',')]) for bomb in input().split()]

for row, col in bombs:
    curr_bomb = bomb_field[row][col]

    if curr_bomb <= 0:
        continue

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < size and 0 <= c < size and bomb_field[r][c] > 0:
                bomb_field[r][c] -= curr_bomb

alive_cells = [num for r in range(size) for num in bomb_field[r] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*bomb_field[r], sep=' ') for r in range(size)]