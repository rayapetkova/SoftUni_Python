def read_next(*args):
    for some in args:
        for el in some:
            yield el


# Test code:

# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')
