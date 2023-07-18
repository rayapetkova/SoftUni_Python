def even_numbers(func):
    def wrapper(numbers):
        result = func(numbers)
        return [n for n in result if n % 2 == 0]

    return wrapper


# Test code:
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))
