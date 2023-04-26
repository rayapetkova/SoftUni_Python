numbers_list = [float(num) for num in input().split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)





#2
#
# numbers_list = [float(num) for num in input().split(", ")]
# result = 1
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(result)
