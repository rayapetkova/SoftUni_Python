electrons = int(input())

n = 1
final = []

while True:
    result = 2 * n**2
    if electrons >= result:
        final.append(result)
        electrons -= result
    else:
        if electrons > 0:
            final.append(electrons)
        break
    n += 1

print(final)






#2
#
# def electron_distribution(electrons):
#     shell = 1
#     lst = []
#     while True:
#         if electrons <= 0:
#             break
#         shell_fill = 2 * shell**2
#         if electrons >= shell_fill:
#             lst.append(shell_fill)
#             electrons -= shell_fill
#         else:
#             lst.append(electrons)
#             electrons = 0
#         shell += 1
#     return lst
#
#
# current_electrons = int(input())
# print(electron_distribution(current_electrons))
