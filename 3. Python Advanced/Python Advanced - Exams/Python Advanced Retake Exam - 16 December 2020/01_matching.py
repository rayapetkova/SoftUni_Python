from collections import deque

males = [int(n) for n in input().split()]
females = deque([int(n) for n in input().split()])

matches = 0

while males and females:
    male, female = males.pop(), females.popleft()

    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0:
        males.pop()
        females.appendleft(female)
        continue

    if female % 25 == 0:
        females.popleft()
        males.append(male)
        continue



    if male == female:
        matches += 1
    else:
        male -= 2
        males.append(male)

print(f"Matches: {matches}")

if not males:
    print(f"Males left: none")
else:
    print(f"Males left: {', '.join(str(m) for m in reversed(males))}")

if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join(str(f) for f in females)}")
