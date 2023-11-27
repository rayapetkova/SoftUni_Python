
def gather_credits(needed_credits, *args):

    current_credits, enrolled_courses = 0, []
    for name, course_credits in args:

        if current_credits >= needed_credits:
            break

        if name in enrolled_courses:
            continue

        enrolled_courses.append(name)
        current_credits += course_credits

    if current_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {current_credits}.\nCourses: {', '.join(c for c in sorted(enrolled_courses))}"

    return f"You need to enroll in more courses! You have to gather {needed_credits - current_credits} credits more."



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
