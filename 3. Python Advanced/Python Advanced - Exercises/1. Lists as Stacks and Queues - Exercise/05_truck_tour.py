from collections import deque

n = int(input())
stack_line = deque()

for i in range(n):
    command = input().split()
    petrol, distance = int(command[0]), int(command[1])
    
    lst = [petrol, distance]
    stack_line.append(lst)

for j in range(n):
    total = 0
    found = True

    for pair in stack_line:
        total = total + pair[0] - pair[1]

        if total < 0:
            stack_line.append(stack_line.popleft())
            found = False
            break

    if found:
        print(j)
        break
