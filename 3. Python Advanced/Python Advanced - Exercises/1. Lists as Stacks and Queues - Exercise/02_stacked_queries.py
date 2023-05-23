def check_stack_line_length(some_stack):
    if some_stack:
        return True
    return False


n = int(input())
stack_line = []

for i in range(n):
    command = input().split()
    if "1" in command:
        stack_line.append(int(command[1]))

    elif check_stack_line_length(stack_line):
        if "2" in command:
            stack_line.pop()
        elif "3" in command:
            print(max(stack_line))
        elif "4" in command:
            print(min(stack_line))

while stack_line:
    element = stack_line.pop()
    if check_stack_line_length(stack_line):
        print(element, end=", ")

    else:
        print(element, end="")