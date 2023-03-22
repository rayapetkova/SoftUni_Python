from datetime import datetime

input_line = list(map(int, input().split("-")))
date1 = datetime(input_line[0], input_line[1], input_line[2])
date2 = datetime(2018, 8, 26)

if date1 > date2:
    print(f"{(date1 - date2).days + 1} days left")
elif date1 < date2:
    print("Passed")
else:
    print(f"Today date")