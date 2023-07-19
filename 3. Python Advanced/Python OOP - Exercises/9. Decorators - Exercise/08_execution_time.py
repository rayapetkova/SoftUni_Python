from time import time


def exec_time(func):
    def wrapper(*args):

        start = time()
        func(*args)
        end = time()

        return end - start

    return wrapper


# Test code:

# @exec_time
# def concatenate(strings):
#     result = ""
#
#     for string in strings:
#         result += string
#
#     return result
#
#
# print(concatenate(["a" for i in range(1000000)]))


# @exec_time
# def loop():
#     count = 0
#
#     for i in range(1, 9999999):
#         count += 1
#
#
# print(loop())
