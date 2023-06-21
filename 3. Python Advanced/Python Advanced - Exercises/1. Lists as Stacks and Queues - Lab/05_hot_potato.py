from collections import deque

names = deque(input().split())
n = int(input()) - 1

idx = 0

while len(names) > 1:
    if idx == n:
        print(f"Removed {names.popleft()}")
        idx = 0
        continue

    idx += 1
    names.rotate(-1)

print(f"Last is {names.popleft()}")