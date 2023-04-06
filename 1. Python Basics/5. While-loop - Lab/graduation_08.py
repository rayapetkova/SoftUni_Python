name = input()
school_class = 0
bad_grades_num = 0
grades_total = 0

while True:
    grade = float(input())
    school_class = school_class + 1

    if grade < 4.00:
        bad_grades_num = bad_grades_num + 1
        if bad_grades_num == 2:
            print(f"{name} has been excluded at {school_class} grade")
            break
        school_class = school_class - 1

    else:
        grades_total = grades_total + grade

    if school_class == 12:
        average_score = grades_total / 12
        print(f"{name} graduated. Average grade: {average_score:.2f}")
        break