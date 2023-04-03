#1

def sum_numbers(a, b):
    return a + b


def subtract(sum_result, c):
    return sum_result - c


current_a = int(input())
current_b = int(input())
current_c = int(input())
current_sum_result = sum_numbers(current_a, current_b)
print(subtract(current_sum_result, current_c))



#2
#
# sum_numbers = lambda a, b: a + b
#
#
# subtract = lambda sum_result, c: sum_result - c
#
#
# current_a = int(input())
# current_b = int(input())
# current_c = int(input())
# current_sum_result = sum_numbers(current_a, current_b)
# print(subtract(current_sum_result, current_c))
