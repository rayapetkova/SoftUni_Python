from collections import deque


def list_manipulator(numbers, second, third, *args):
    numbers = deque(numbers)

    if second == "add":
        if third == "beginning":
            [numbers.appendleft(num) for num in args[::-1]]

        elif third == "end":
            numbers.extend(args)

    elif second == "remove":
        if third == "beginning":
            if args:
                for i in range(args[0]):
                    numbers.popleft()
            else:
                numbers.popleft()

        elif third == "end":
            if args:
                for i in range(args[0]):
                    numbers.pop()
            else:
                numbers.pop()

    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
