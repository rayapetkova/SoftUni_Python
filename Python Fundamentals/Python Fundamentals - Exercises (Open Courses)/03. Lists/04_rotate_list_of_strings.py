strings = input().split()
strings.insert(0, strings[-1])
strings.pop()

print(*strings, sep=" ")