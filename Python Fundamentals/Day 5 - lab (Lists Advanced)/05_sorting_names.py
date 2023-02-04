students = input().split(", ")

sorted_by_letters = sorted(students)

sorted_students = sorted(sorted_by_letters, key=len, reverse=True)
print(sorted_students)
