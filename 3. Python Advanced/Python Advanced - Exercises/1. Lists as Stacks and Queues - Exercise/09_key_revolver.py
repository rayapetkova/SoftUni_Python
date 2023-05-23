from collections import deque

price_each_bullet = int(input())
gun_size = int(input())
gun_barrel_size = gun_size

bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence = int(input())

total_bullets = 0

while True:
    if gun_barrel_size == 0 and bullets:
        gun_barrel_size = gun_size
        print(f"Reloading!")

    if bullets:
        bullet = bullets.pop()
        if bullet <= locks[0]:
            locks.popleft()
            print(f"Bang!")
        else:
            print(f"Ping!")
        gun_barrel_size -= 1
        total_bullets += 1

    if not locks:
        if bullets and gun_barrel_size == 0:
            print("Reloading!")

        earned = intelligence - (total_bullets * price_each_bullet)
        print(f"{len(bullets)} bullets left. Earned ${earned}")
        break

    if not bullets:
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
