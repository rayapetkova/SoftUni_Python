first = int(input())
second = int(input())
third = int(input())
students = int(input())

students_per_hour = first + second + third

hours = 0

while True:
    if students <= 0:
        break
    hours += 1
    students -= students_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")