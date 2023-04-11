size = int(input())
matrix = []

for row in range(size):
    numbers = [int(n) for n in input().split()]
    matrix.append(numbers)

sum_diagonal = 0
for row in range(size):
    for col in range(size):
        if row == col:
            sum_diagonal += matrix[row][col]

print(sum_diagonal)






#2
#
# size = int(input())
# matrix = []
#
# for row in range(size):
#     numbers = [int(n) for n in input().split()]
#     matrix.append(numbers)
#
# sum_diagonal = 0
# for idx in range(size):
#     sum_diagonal += matrix[idx][idx]
#
# print(sum_diagonal)
