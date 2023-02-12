elements = input().split()

moves = 0

while True:
    line = input()
    if line == "end":
        if len(elements) > 0:
            print(f"Sorry you lose :(")
            print(*elements, sep=" ")
        elif len(elements) <= 0:
            print(f"You have won in {moves} turns!")
        break
    command = line.split()
    first = int(command[0])
    second = int(command[1])
    if len(elements) <= 0:
        continue
    moves += 1
    if first == second or first < 0 or first >= len(elements) or second < 0 or second >= len(elements):
        middle = int(len(elements) // 2)
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")
        print(f"Invalid input! Adding additional elements to the board")
    elif elements[first] == elements[second] and first != second:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        if first < second:
            elements.pop(second)
            elements.pop(first)
        elif second < first:
            elements.pop(first)
            elements.pop(second)
    elif elements[first] != elements[second]:
        print(f"Try again!")