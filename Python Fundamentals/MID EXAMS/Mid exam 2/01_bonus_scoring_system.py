from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

bonuses = []
find_max = []

for i in range(students):
    attendances = int(input())
    find_max.append(attendances)
    bonus = (attendances / lectures) * (5 + additional_bonus)
    bonuses.append(bonus)

max_lectures = max(find_max)
max_bonus = max(bonuses)

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")