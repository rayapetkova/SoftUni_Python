def find_tunnel_start_and_end(curr_matrix):
    c_tunnel = []
    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "T":
                c_tunnel.append((r, c))
    return c_tunnel


SIZE, racing_number = int(input()), input()
matrix = [input().split() for i in range(SIZE)]

directions = {
    'left': (0, -1),
    'right': (0, +1),
    'up': (-1, 0),
    'down': (+1, 0)
}

car = (0, 0)
km_passed = 0
tunnel = find_tunnel_start_and_end(matrix)

while True:
    direction = input()
    if direction == "End":
        print(f"Racing car {racing_number} DNF.")
        matrix[car[0]][car[1]] = "C"
        break
    row, col = car[0] + directions[direction][0], car[1] + directions[direction][1]
    if matrix[row][col] == "T":
        tunnel.remove((row, col))
        pos = tunnel[0]
        car = pos
        km_passed += 30
        matrix[row][col], matrix[pos[0]][pos[1]] = ".", "."
    elif matrix[row][col] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        km_passed += 10
        matrix[row][col] = "C"
        break
    else:
        km_passed += 10
        car = (row, col)

print(f"Distance covered {km_passed} km.")
[print(''.join(nested)) for nested in matrix]