text = list(input())
stack_line = []

while text:
    stack_line.append(text.pop())

print("".join(stack_line))




#2
#
# text = list(input())
# stack_line = []
#
# for el in range(len(text)):
#     stack_line.append(text.pop())
#
# print("".join(stack_line))
