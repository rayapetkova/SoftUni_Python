def multiply(*args):
    total = 1
    for el in args:
        total *= el
    return total


# Test inputs:
# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))
