rows = int(input())
matrix = [[int(n) for n in input().split()] for i in range(rows)]

squares = input().split()

attacked_ships = 0

for square in squares:
    row, col = [int(n) for n in square.split("-")]

    if matrix[row][col]:
        matrix[row][col] -= 1

        if matrix[row][col] == 0:
            attacked_ships += 1

print(attacked_ships)
