def is_path_exist(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Check boundary conditions
    if maze[0][0] == 0 or maze[rows - 1][cols - 1] == 0:
        return "No path exists"

    visited = set()  # To keep track of visited cells

    # Directions: up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # DFS to find a path
    def dfs(x, y):
        if (x, y) == (rows - 1, cols - 1):
            return True

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                if dfs(nx, ny):
                    return True
        return False

    if dfs(0, 0):
        return "Path exists"
    else:
        return "No path exists"


# Reading input from the console
maze = []
while True:
    row = input().strip()
    if row == "Finish":
        break
    maze.append([int(x) for x in row.split(', ')])

# Checking if a path exists
if maze:
    print(is_path_exist(maze))
