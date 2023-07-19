def even_parameters(func):
    def wrapper(*args):

        for el in args:
            if not isinstance(el, int) or el % 2 != 0:
                return f"Please use only even numbers!"

        return func(*args)

    return wrapper


# Test code:

# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))
