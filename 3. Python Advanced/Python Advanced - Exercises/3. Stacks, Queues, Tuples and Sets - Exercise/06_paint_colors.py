from collections import deque

text = deque(input().split())

colors = ["red", "yellow", "blue", "orange", "purple", "green"]
creations = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
final = []

while len(text) > 0:
    if len(text) == 1:
        last_colour = text.pop()
        if last_colour in colors:
            final.append(last_colour)
        continue

    first, second = text.popleft(), text.pop()

    if first + second in colors:
        final.append(first + second)

    elif second + first in colors:
        final.append(second + first)

    else:
        first, second = first[:-1], second[:-1]
        middle = len(text) // 2
        if first != "":
            text.insert(middle, first)
        if second != "":
            text.insert(middle, second)

for color in final:
    if color in creations.keys():
        for element in creations[color]:
            if element not in final:
                final.remove(color)

print(final)
