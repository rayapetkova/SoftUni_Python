from collections import deque


def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes = deque(args)
    while True:
        cube = cubes.popleft()
        if cube == "Finish":
            cubes.clear()
            break
        if box_size < cube:
            cube -= box_size
            cubes.appendleft(cube)
            box_size = 0
            break
        box_size -= cube
    if box_size:
        return f"There is free space in the box. You could put {box_size} more cubes."
    cubes.pop() if cubes else None
    return f"No more free space! You have {sum(cubes)} more cubes."


# Test inputs:
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
