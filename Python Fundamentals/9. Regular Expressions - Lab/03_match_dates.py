import re

all_dates = input()

pattern = r"\b(?P<day>\d{2})([/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
valid_dates = re.finditer(pattern, all_dates)

for date in valid_dates:
    print(f"Day: {date.group('day')}, Month: {date.group('month')}, Year: {date.group('year')}")