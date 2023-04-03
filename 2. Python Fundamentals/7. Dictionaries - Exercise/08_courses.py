students = {}

while True:
    line = input()
    if line == "end":
        break
    course, course_name = line.split(" : ")
    students[course] = students.get(course, []) + [course_name]

for key, value in students.items():
    print(f"{key}: {len(value)}")
    [print(f"-- {name}") for name in value]