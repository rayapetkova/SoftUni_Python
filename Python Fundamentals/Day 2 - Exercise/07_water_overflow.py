n = int(input())
tank = 0

for i in range(1, n + 1):
    water = int(input())
    if tank + water > 255:
        print("Insufficient capacity!")
    else:
        tank += water

print(tank)