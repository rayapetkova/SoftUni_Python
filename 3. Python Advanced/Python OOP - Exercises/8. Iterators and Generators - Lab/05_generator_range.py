def genrange(start, end):
    while start <= end:
        yield start
        start += 1


# Test code:
# print(list(genrange(1, 10)))
