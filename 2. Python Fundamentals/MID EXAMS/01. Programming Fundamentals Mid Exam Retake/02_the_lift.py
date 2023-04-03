people_waiting = int(input())
lift = list(map(int, input().split()))

for i in lift:
    idx_i = lift.index(i)
    while lift[idx_i] < 4 and people_waiting > 0:
        people_waiting -= 1
        lift[idx_i] += 1

if people_waiting == 0 and (1 in lift or 2 in lift or 3 in lift):
    print(f"The lift has empty spots!")
    print(*lift, sep=" ")

elif people_waiting > 0 and lift.count(4) == len(lift):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift, sep=" ")

elif people_waiting == 0 and lift.count(4) == len(lift):
    print(*lift, sep=" ")