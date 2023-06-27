hours = int(input())
minutes = int(input())

hours_in_minutes = hours * 60
all_minutes = (hours_in_minutes + minutes) + 15
hours1 = all_minutes // 60
minutes1 = all_minutes % 60

if hours1 == 24:
    hours1 = 0
if minutes1 < 10:
    print(f"{hours1}:0{minutes1}")
else:
    print(f"{hours1}:{minutes1}")
