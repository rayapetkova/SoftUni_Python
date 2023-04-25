def recursive_power(num, power):
    if power == 0:
        return 1
    return num * recursive_power(num, power - 1)


# Test inputs:
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))





#2 - solution without recursion
#
# def recursive_power(number, power):
#     return number ** power
