def explosion(curr_matrix, damage, all_moves, cell_row, cell_col):
    for move in all_moves:
        position_row, position_col = cell_row + move[0], cell_col + move[1]

        if 0 <= position_row < SIZE and 0 <= position_col < SIZE and curr_matrix[position_row][position_col] > 0:
            curr_matrix[position_row][position_col] -= damage


SIZE = int(input())
matrix = [[int(n) for n in input().split()] for _ in range(SIZE)]
cells_bombs = [[int(n) for n in x.split(",")] for x in input().split()]

moves = (
    (-1, -1),  # top left
    (-1, 0),  # top
    (-1, +1),  # top right
    (0, -1),  # left
    (0, +1),  # right
    (+1, -1),  # bottom left
    (+1, 0),  # bottom
    (+1, +1),  # bottom right
    (0, 0)  # current cell position
)

for cell in cells_bombs:
    row, col = cell[0], cell[1]
    if matrix[row][col] <= 0:
        continue

    damage_cell = matrix[row][col]
    explosion(matrix, damage_cell, moves, row, col)

alive_cells = [number for curr_row in range(SIZE) for number in matrix[curr_row] if number > 0]
print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
print(*[' '.join(str(n) for n in nested) for nested in matrix], sep="\n")







# 2 - solution without many comprehensions
#
# def explosion(curr_matrix, all_cells, curr_row, curr_col, damage_bomb):
#     for cell in all_cells:
#         if 0 <= curr_row + cell[0] < rows and 0 <= curr_col + cell[1] < rows:
#             if curr_matrix[curr_row + cell[0]][curr_col + cell[1]] > 0:
#                 curr_matrix[curr_row + cell[0]][curr_col + cell[1]] -= damage_bomb
#
#
# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     numbers = [int(n) for n in input().split()]
#     matrix.append(numbers)
#
# coordinates = input().split()
#
# all_coordinates = []
# for each in coordinates:
#     row, col = each.split(",")
#     all_coordinates.append((int(row), int(col)))
#
# cells = (
#     (-1, -1),  # top left diagonal
#     (-1, 0),  # top
#     (-1, +1),  # top right diagonal
#     (0, -1),  # left
#     (0, +1),  # right
#     (+1, -1),  # bottom left diagonal
#     (+1, 0),  # bottom
#     (+1, +1)  # bottom right diagonal
# )
#
# for coordinate in all_coordinates:
#     if matrix[coordinate[0]][coordinate[1]] <= 0:
#         continue
#     damage = matrix[coordinate[0]][coordinate[1]]
#     matrix[coordinate[0]][coordinate[1]] = 0
#     explosion(matrix, cells, coordinate[0], coordinate[1], damage)
#
# alive_cells, sum_alive_cells = 0, 0
# for nested_lst in matrix:
#     for el in nested_lst:
#         if el > 0:
#             alive_cells += 1
#             sum_alive_cells += el
#
# print(f"Alive cells: {alive_cells}\nSum: {sum_alive_cells}")
# for nested_lst in matrix:
#     print(*nested_lst, sep=" ")
