students = int(input())

top_students = 0
second_grade_students = 0
third_grade_students = 0
failed_students = 0
top_grades = 0
second_grades = 0
third_grades = 0
failes_grades = 0

for i in range(1, students + 1):
    grade = float(input())
    if grade >= 5.00:
        top_students = top_students + 1
        top_grades = top_grades + grade
    elif 4.00 <= grade <= 4.99:
        second_grade_students = second_grade_students + 1
        second_grades = second_grades + grade
    elif 3.00 <= grade <= 3.99:
        third_grade_students = third_grade_students + 1
        third_grades = third_grades + grade
    elif grade < 3.00:
        failed_students = failed_students + 1
        failes_grades = failes_grades + grade

top_students_percents = (top_students / students) * 100
print(f"Top students: {top_students_percents:.2f}%")

second_grade_percents = (second_grade_students / students) * 100
print(f"Between 4.00 and 4.99: {second_grade_percents:.2f}%")

third_grade_percents = (third_grade_students / students) * 100
print(f"Between 3.00 and 3.99: {third_grade_percents:.2f}%")

failed_percents = (failed_students / students) * 100
print(f"Fail: {failed_percents:.2f}%")

average_score = (top_grades + second_grades + third_grades + failes_grades) / students
print(f"Average: {average_score:.2f}")