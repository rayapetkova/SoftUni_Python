from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendances = 0

for i in range(students):
    attendances = int(input())
    bonus = (attendances / lectures) * (5 + additional_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        max_attendances = attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")