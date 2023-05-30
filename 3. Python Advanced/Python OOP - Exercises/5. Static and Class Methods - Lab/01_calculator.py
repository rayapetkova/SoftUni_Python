import operator
from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(operator.mul, args)

    @staticmethod
    def divide(*args):
        return reduce(operator.truediv, args)

    @staticmethod
    def subtract(*args):
        return reduce(operator.sub, args)


# Test code:

# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
