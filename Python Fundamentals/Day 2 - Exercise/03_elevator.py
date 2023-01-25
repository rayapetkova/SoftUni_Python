people = int(input())
capacity = int(input())

first = people // capacity
courses = first

result = people / capacity
if not result.is_integer():
    courses += 1

print(courses)