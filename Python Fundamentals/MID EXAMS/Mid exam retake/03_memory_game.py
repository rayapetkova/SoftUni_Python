elements = input().split()

moves = 0

while True:
    line = input()
    if line == "end":
        if len(elements) <= 0:
            print(f"You have won in {moves} turns!")
        else:
            print(f"Sorry you lose :(")
            print(*elements, sep=" ")
        break
    if len(elements) <= 0:
        continue
    command = line.split()
    first = int(command[0])
    second = int(command[1])
    moves += 1
    if elements[first] == elements[second] and first != second:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        elements.pop(first)
        elements.pop(second - 1)
    elif first == second or (first < 0 or second < 0) or (first >= len(elements) or second >= len(elements)):
        middle = int(len(elements) / 2)
        elements.insert(middle, f"{moves}a")
        elements.insert(middle + 1, f"{moves}a")
        print(f"Invalid input! Adding additional elements to the board")
    elif elements[first] != elements[second]:
        print(f"Try again!")