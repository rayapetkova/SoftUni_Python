from datetime import datetime, timedelta
from collections import deque

robots_dict = {}

robots_input = input().split(";")
for robot in robots_input:
    current_robot = robot.split("-")
    name, processing_time = current_robot[0], int(current_robot[1])
    robots_dict[name] = [processing_time, 0]


starting_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    c_product = input()
    if c_product == "End":
        break

    products.append(c_product)

while products:
    starting_time += timedelta(seconds=1)
    product = products.popleft()

    free_robots = deque()
    for name, curr_list in robots_dict.items():
        if curr_list[1] != 0:
            robots_dict[name][1] -= 1
        if curr_list[1] == 0:
            free_robots.append(name)

    if not free_robots:
        products.append(product)
        continue

    first_free_robot = free_robots.popleft()
    robots_dict[first_free_robot][1] = robots_dict[first_free_robot][0]

    print(f"{first_free_robot} - {product} [{starting_time.strftime('%H:%M:%S')}]")