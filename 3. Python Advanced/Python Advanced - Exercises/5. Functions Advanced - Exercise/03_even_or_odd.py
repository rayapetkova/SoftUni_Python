def even_odd(*args):
    if args[-1] == "even":
        return [num for num in args[:-1] if num % 2 == 0]
    return [num for num in args[:-1] if num % 2 != 0]


# Test inputs:
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
