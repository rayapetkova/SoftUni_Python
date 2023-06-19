def squares(n):
    start = 1

    while start <= n:
        yield start ** 2
        start += 1


# Test code:
# print(list(squares(5)))
