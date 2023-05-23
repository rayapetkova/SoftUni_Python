expression = input()
stack_line = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack_line.append(i)

    elif expression[i] == ")":
        start = stack_line.pop()
        print(expression[start:i + 1])





#2
#
# expression = input()
# stack_line = []
#
# for i in range(len(expression)):
#     if expression[i] == "(":
#         stack_line.append(i)
#     elif expression[i] == ")":
#         start = stack_line.pop()
#         print(expression[start:i + 1])
