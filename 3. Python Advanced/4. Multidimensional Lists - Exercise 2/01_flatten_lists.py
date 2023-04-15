numbers = input().split("|")
matrix = [[num for num in lst.split()] for lst in numbers][::-1]
[matrix[0].extend(nested) for nested in matrix[1:]]
print(" ".join(matrix[0]))





#2
#
# numbers = input().split("|")
# matrix = [[num for num in lst.split()] for lst in numbers][::-1]
# for nested in matrix[1:]:
#     matrix[0].extend(nested)
# print(" ".join(matrix[0]))
