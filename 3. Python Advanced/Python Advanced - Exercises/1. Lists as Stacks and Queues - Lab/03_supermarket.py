from collections import deque

people = deque()

while True:
    name = input()

    if name == "End":
        print(f"{len(people)} people remaining.")
        break

    if name == "Paid":
        while people:
            print(people.popleft())
        continue

    people.append(name)
