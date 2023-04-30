def students_credits(*args):
    dictionary = {}
    for each in args:
        line = each.split("-")
        course, credits, max_test_points, points = line[0], int(line[1]), int(line[2]), int(line[3])
        percent = points / max_test_points
        credit = credits * percent
        dictionary[course] = credit
    sorted_courses = sorted(dictionary.items(), key=lambda x: -x[1])
    printed_result = '\n'.join([f"{course_name} - {diyans_credits:.1f}" for course_name, diyans_credits in sorted_courses])
    if sum(dictionary.values()) >= 240:
        return f"Diyan gets a diploma with {sum(dictionary.values()):.1f} credits.\n{printed_result}"
    else:
        return f"Diyan needs {240 - sum(dictionary.values()):.1f} credits more for a diploma.\n{printed_result}"


# Test inputs:

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )


# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
