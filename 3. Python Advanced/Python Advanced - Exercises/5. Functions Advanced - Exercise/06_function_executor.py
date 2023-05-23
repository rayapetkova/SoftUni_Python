def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    final = []
    
    for some_func, parameters in args:
        final.append(f"{some_func.__name__} - {some_func(*parameters)}")
    
    return '\n'.join(final)


# Test code:

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
