from collections import deque


def best_list_pureness(lst, k):
    lst = deque(lst)

    rotation = 0
    rotations, best_pureness = 1, sum([lst[i] * i for i in range(len(lst))])

    for i in range(k):
        lst.rotate()
        total = sum([lst[i] * i for i in range(len(lst))])

        if total > best_pureness:
            best_pureness = total
            rotation = rotations

        rotations += 1

    return f"Best pureness {best_pureness} after {rotation} rotations"


# Test codes:

# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
