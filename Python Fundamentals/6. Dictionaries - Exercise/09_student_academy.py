num = int(input())
good_students = {}

for _ in range(num):
    student_name = input()
    student_grade = float(input())
    good_students[student_name] = good_students.get(student_name, []) + [student_grade]

[print(f"{name} -> {(sum(grade) / len(grade)):.2f}") for name, grade in good_students.items() if (sum(grade) / len(grade)) >= 4.50]