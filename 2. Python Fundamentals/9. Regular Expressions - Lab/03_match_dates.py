import re

all_dates = input()

pattern = r"\b(?P<day>\d{2})([/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
valid_dates = re.finditer(pattern, all_dates)

for date in valid_dates:
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")




#2
#
# import re
#
# all_dates = input()
#
# pattern = r"\b(\d{2})([/.-])([A-Z][a-z]{2})\2(\d{4})\b"
# valid_dates = re.finditer(pattern, all_dates)
#
# for date in valid_dates:
#     print(f"Day: {date[1]}, Month: {date[3]}, Year: {date[4]}")
