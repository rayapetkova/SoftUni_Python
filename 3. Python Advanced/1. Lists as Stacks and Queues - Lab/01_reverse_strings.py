text = list(input())
stack_line = []

for el in range(len(text)):
    stack_line.append(text.pop())

print("".join(stack_line))