from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
total_cars_passed = 0

while True:
    line = input()

    if line == "END":
        break
    if line != "green":
        cars.append(line)

    elif line == "green":
        current_green_light = green_light

        while current_green_light > 0 and cars:
            car = cars.popleft()

            time_to_pass = current_green_light + free_window

            if len(car) > time_to_pass:
                print(f"A crash happened!\n{car} was hit at {car[time_to_pass]}.")
                exit()

            total_cars_passed += 1
            current_green_light -= len(car)

print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")