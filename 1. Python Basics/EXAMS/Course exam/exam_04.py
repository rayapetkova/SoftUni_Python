students = int(input())

top_students = 0
students_4 = 0
students_3 = 0
fail_students = 0
all_grades = 0

for i in range(1, students + 1):
    grade = float(input())
    if grade >= 5.00:
        top_students = top_students + 1
    elif 4.00 <= grade < 5.00:
        students_4 = students_4 + 1
    elif 3.00 <= grade < 4.00:
        students_3 = students_3 + 1
    elif 2.00 <= grade < 3.00:
        fail_students = fail_students + 1
    all_grades = all_grades + grade

average = all_grades / students

print(f"Top students: {((top_students / students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((students_4 / students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((students_3 / students) * 100):.2f}%")
print(f"Fail: {((fail_students / students) * 100):.2f}%")
print(f"Average: {average:.2f}")