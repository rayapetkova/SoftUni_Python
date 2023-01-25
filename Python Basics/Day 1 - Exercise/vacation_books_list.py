pages_number = int(input())
pages_read_for_one_hour = int(input())
days_number = int(input())

all_hours = pages_number // pages_read_for_one_hour
hours_per_day = int(all_hours / days_number)

print(hours_per_day)