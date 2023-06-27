from math import floor

world_record = float(input())
distance_in_m = float(input())
one_meter_time = float(input())

all_seconds = one_meter_time * distance_in_m
delay = floor(distance_in_m / 15)
seconds_with_delay = delay * 12.5
all_seconds_with_delay = all_seconds + seconds_with_delay

if all_seconds_with_delay < world_record:
    print(f"Yes, he succeeded! The new world record is {all_seconds_with_delay:.2f} seconds.")
elif all_seconds_with_delay >= world_record:
    print(f"No, he failed! He was {(all_seconds_with_delay - world_record):.2f} seconds slower.")
