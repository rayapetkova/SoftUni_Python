from itertools import permutations


def possible_permutations(numbers):
    all_permutations = list(permutations(numbers))

    for perm in all_permutations:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
