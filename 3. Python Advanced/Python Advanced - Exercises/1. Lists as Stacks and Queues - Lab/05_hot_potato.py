from collections import deque

names = deque(input().split())
n = int(input()) - 1

idx = 0
while len(names) > 1:
    name = names.popleft()
    if idx == n:
        print(f"Removed {name}")
        idx = 0
        continue
    idx += 1
    names.append(name)

print(f"Last is {names.popleft()}")