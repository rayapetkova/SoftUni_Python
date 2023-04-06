jury = int(input())
all_sum = 0
counter_grades = 0
all_grades = 0

while True:
    title = input()

    if title == "Finish":
        average = all_grades / counter_grades
        print(f"Student's final assessment is {average:.2f}.")
        break

    sum_grades = 0
    for i in range(1, jury + 1):
        grade = float(input())
        counter_grades = counter_grades + 1
        sum_grades = sum_grades + grade
        all_grades = all_grades + grade

    average_sum_grades = sum_grades / jury
    print(f"{title} - {average_sum_grades:.2f}.")