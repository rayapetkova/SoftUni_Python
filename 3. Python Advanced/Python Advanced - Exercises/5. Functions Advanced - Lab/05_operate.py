from functools import reduce
import operator


def operate(c_operator, *args):
    operations = {
        "+": reduce(operator.add, args),
        "-": reduce(operator.sub, args),
        "*": reduce(operator.mul, args),
        "/": reduce(operator.truediv, args)
    }
    return operations[c_operator]


# Test inputs:
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))





#2
#
# def operate(operator, *args):
#     total = 1
#     if operator == "+":
#         total = sum(args)
#     elif operator == "-":
#         total = args[0]
#         for num in args[1:]:
#             total -= num
#     elif operator == "*":
#         for num in args:
#             total *= num
#     elif operator == "/":
#         total = args[0]
#         for num in args[1:]:
#             total /= num
#     return total
