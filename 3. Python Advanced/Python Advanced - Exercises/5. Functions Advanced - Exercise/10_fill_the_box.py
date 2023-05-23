from collections import deque


def fill_the_box(height, length, width, *args):
    capacity = height * length * width
    cubes = deque(args)

    while cubes:
        cube = cubes.popleft()

        if cube == "Finish":
            break

        if capacity < cube:
            cube -= capacity
            cubes.appendleft(cube)
            capacity = 0
            break

        capacity -= cube

    if capacity > 0:
        return f"There is free space in the box. You could put {capacity} more cubes."

    idx_finish = cubes.index("Finish")
    return f"No more free space! You have {sum(list(cubes)[:idx_finish])} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
