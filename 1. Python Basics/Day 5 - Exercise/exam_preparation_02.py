bad_grades = int(input())

bad_grades_marin = 0
all_score = 0
grades_number = 0
last_task = ""
bad_grades_flag = False

while True:
    task_name = input()
    if task_name == "Enough":
        break
    task_grade = int(input())
    all_score = all_score + task_grade
    grades_number = grades_number + 1

    if task_grade <= 4:
        bad_grades_marin = bad_grades_marin + 1
        if bad_grades_marin >= bad_grades:
            bad_grades_flag = True
            break

    last_task = task_name


if bad_grades_flag:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_score = all_score / grades_number
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {grades_number}")
    print(f"Last problem: {last_task}")