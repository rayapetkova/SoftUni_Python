from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    idx = 0

    while numbers:
        number = numbers.popleft()
        if idx == 0:
            kwargs['a'] += number

        elif idx == 1:
            kwargs['s'] -= number

        elif idx == 2:
            if number == 0:
                idx += 1
                continue

            kwargs['d'] /= number

        elif idx == 3:
            kwargs['m'] *= number
            idx = 0
            continue

        idx += 1

    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    final = []
    for key, value in sorted_dict:
        final.append(f"{key}: {value:.1f}")

    return "\n".join(final)


# Test inputs:
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
