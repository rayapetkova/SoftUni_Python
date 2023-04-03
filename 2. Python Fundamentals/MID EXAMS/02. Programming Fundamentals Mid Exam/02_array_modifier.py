numbers = [int(i) for i in input().split()]

while True:
    command1 = input()
    if command1 == "end":
        break
    command = command1.split()
    if "swap" in command:
        first = int(command[1])
        second = int(command[2])
        numbers[first], numbers[second] = numbers[second], numbers[first]
    elif "multiply" in command:
        first = int(command[1])
        second = int(command[2])
        numbers[first] = numbers[first] * numbers[second]
    elif "decrease" in command:
        for i in numbers:
            idx_i = numbers.index(i)
            numbers[idx_i] -= 1

print(*numbers, sep=", ")