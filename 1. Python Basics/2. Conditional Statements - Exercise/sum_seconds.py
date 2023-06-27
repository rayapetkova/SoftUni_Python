time_first = int(input())
time_second = int(input())
time_third = int(input())

all_time_in_sec = time_first + time_second + time_third
all_time_in_min = all_time_in_sec // 60
all_time_in_sec1 = all_time_in_sec % 60

if all_time_in_sec1 < 10:
    print(f"{all_time_in_min}:0{all_time_in_sec1}")
else:
    print(f"{all_time_in_min}:{all_time_in_sec1}")
