def multiply(times):
    def decorator(func):

        def wrapper(number):
            result = func(number)
            return result * times

        return wrapper

    return decorator


# Test code:
#
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
#
# print(add_ten(3))
