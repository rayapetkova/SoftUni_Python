n = int(input())
word = input()
strings = []

for i in range(n):
    current_string = input()
    strings.append(current_string)

print(strings)

for j in range(len(strings) - 1, -1, -1):
    element = strings[j]
    if word not in element:
        strings.remove(element)

print(strings)