from collections import deque


def return_not_bullets_not_locks(curr_intelligence, all_bullets, one_bullet_price, bullets_stack):
    earned = curr_intelligence - (all_bullets * one_bullet_price)
    return f"{len(bullets_stack)} bullets left. Earned ${earned}"


def return_not_bullets_locks(curr_locks):
    return f"Couldn't get through. Locks left: {len(curr_locks)}"


price_each_bullet = int(input())
gun_size = int(input())
gun_barrel_size = gun_size
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence = int(input())
total_bullets = 0

while True:
    if gun_barrel_size == 0:
        if not bullets and locks:
            print(return_not_bullets_locks(locks))
            break
        elif not bullets and not locks:
            print(return_not_bullets_not_locks(intelligence, total_bullets, price_each_bullet, bullets))
            break
        else:
            gun_barrel_size = gun_size
            print(f"Reloading!")
    if (not locks and bullets) or (not locks and not bullets):
        print(return_not_bullets_not_locks(intelligence, total_bullets, price_each_bullet, bullets))
        break
    elif not bullets and locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    elif bullets:
        bullet = bullets.pop()
        gun_barrel_size -= 1
        total_bullets += 1
        if bullet <= locks[0]:
            locks.popleft()
            print(f"Bang!")
        else:
            print(f"Ping!")
