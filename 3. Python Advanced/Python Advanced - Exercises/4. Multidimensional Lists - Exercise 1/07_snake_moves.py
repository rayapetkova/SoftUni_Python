from collections import deque

rows, cols = [int(n) for n in input().split()]
text = list(input())
text_copy = deque(text.copy())

for row in range(rows):
    while len(text_copy) < cols:
        text_copy.extend(text)

    if row % 2 == 0:
        print(*[text_copy.popleft() for c in range(cols)], sep="")
    else:
        print(*[text_copy.popleft() for c in range(cols)][::-1], sep="")