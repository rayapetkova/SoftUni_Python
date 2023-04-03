input_times = input().split()

half = len(input_times) // 2
first_car_half = input_times[0:half] # [start : end]
int_first_car_half = [int(k) for k in first_car_half]

second_car_half = input_times[-1:half:-1] # [start : end : by step] --> [from -1 : to half : by step -1]
int_second_car_half = [int(m) for m in second_car_half]

time_first_car = 0
time_second_car = 0

for i in int_first_car_half:
    time_first_car += i
    if i == 0:
        time_first_car *= 0.80

for n in int_second_car_half:
    time_second_car += n
    if n == 0:
        time_second_car *= 0.8

if time_first_car < time_second_car:
    print(f"The winner is left with total time: {time_first_car:.1f}")
else:
    print(f"The winner is right with total time: {time_second_car:.1f}")