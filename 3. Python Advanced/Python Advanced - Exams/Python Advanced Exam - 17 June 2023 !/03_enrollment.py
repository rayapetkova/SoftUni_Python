def gather_credits(number, *args):
    courses = []
    total_credits = 0

    for course, credits in args:
        if number <= 0:
            break

        if course in courses:
            continue

        number -= credits
        courses.append(course)
        total_credits += credits

    final = []

    if number <= 0:
        final.append(f"Enrollment finished! Maximum credits: {total_credits}.")

        final.append(f"Courses: {', '.join([c for c in sorted(courses)])}")

    else:
        return f"You need to enroll in more courses! You have to gather {number} credits more."

    return "\n".join(final)


# Test code:

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
#
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
