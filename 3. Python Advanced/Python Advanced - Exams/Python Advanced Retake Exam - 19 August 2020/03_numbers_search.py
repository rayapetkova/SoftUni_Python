def numbers_searching(*args):
    duplicates = []

    for el in args:
        counter = args.count(el)

        if counter > 1:
            duplicates.append(el)

    new_set = set(duplicates)

    sorted_lst = sorted(args)
    missing_number = 0

    for n in range(sorted_lst[0], sorted_lst[-1] + 1):
        if n not in sorted_lst:
            missing_number = n

    return [missing_number, sorted(list(new_set))]


# Test code:

# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
