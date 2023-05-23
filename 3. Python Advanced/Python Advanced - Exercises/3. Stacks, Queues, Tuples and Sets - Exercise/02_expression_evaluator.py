from functools import reduce
from math import floor

expression = input().split()
symbols = "*+-/"

dictionary_symbols = {
    "*": lambda i: reduce(lambda a, b: a * b, [int(n) for n in expression[:i]]),
    "+": lambda i: reduce(lambda a, b: a + b, [int(n) for n in expression[:i]]),
    "-": lambda i: reduce(lambda a, b: a - b, [int(n) for n in expression[:i]]),
    "/": lambda i: reduce(lambda a, b: floor(a / b), [int(n) for n in expression[:i]])
}

idx = 0
while len(expression) > 1:
    for el in expression:
        if str(el) in symbols:
            idx = expression.index(el)
            number = dictionary_symbols[el](idx)
            del expression[:idx + 1]
            expression.insert(0, number)
            idx = 0
            break

        idx += 1

print(*expression, sep="")





#2
#
# from math import floor
#
# expression = input().split()
# symbols = "*+-/"
#
# idx = 0
# while len(expression) > 1:
#     result = []
#     for el in expression:
#         result.append(el)
#         if str(el) in symbols:
#             idx_symbol = expression.index(el)
#             result[0] = int(result[0])
#             nums = [int(n) for n in result[1:len(result) - 1]]
#             while nums:
#                 if el == "*":
#                     result[0] *= nums.pop(0)
#                 elif el == "+":
#                     result[0] += nums.pop(0)
#                 elif el == "-":
#                     result[0] -= nums.pop(0)
#                 elif el == "/":
#                     result[0] /= nums.pop(0)
#             del expression[:idx_symbol + 1]
#             final = floor(result.pop(0))
#             expression.insert(0, str(final))
#             break
#
# print(*expression, sep="")
