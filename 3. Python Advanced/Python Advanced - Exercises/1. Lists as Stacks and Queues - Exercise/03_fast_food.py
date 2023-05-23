from collections import deque

quantity = int(input())
orders = deque(list(map(int, input().split())))

print(max(orders))

while orders:
    some_order = orders.popleft()
    if some_order <= quantity:
        quantity -= some_order

    else:
        orders.appendleft(some_order)
        break

if orders:
    print(f"Orders left: {' '.join(str(n) for n in orders)}")
else:
    print(f"Orders complete")