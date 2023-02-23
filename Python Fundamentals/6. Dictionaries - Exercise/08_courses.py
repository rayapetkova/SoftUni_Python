students = {}

while True:
    line = input()
    if line == "end":
        break
    command = line.split(" : ")
    course = command[0]
    course_name = command[1]
    students[course] = students.get(course, []) + [course_name]

for key, value in students.items():
    print(f"{key}: {len(value)}")
    [print(f"-- {name}") for name in value]