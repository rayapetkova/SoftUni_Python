def add(title, lessons):
    if title not in lessons:
        lessons.append(title)
    return lessons


def insert_el(title, idx, lessons):
    if title not in lessons:
        lessons.insert(idx, title)
    return lessons


def remove_el(title, lessons):
    title_index = lessons.index(title)
    if title in lessons:
        if f"{title}-Exercise" in lessons:
            lessons.pop(title_index + 1)
            lessons.remove(title)
        else:
            lessons.remove(title)
    return lessons


def swap_el(title1, title2, lessons):
    if title1 in lessons and title2 in lessons:
        first_title = lessons.index(title1)
        second_title = lessons.index(title2)

        lessons[first_title], lessons[second_title] = lessons[second_title], lessons[first_title]

        first_exercise = f"{title1}-Exercise"
        second_exercise = f"{title2}-Exercise"

        if first_exercise in lessons:
            lessons.remove(first_exercise)
            lessons.insert(lessons.index(title1) + 1, first_exercise)
        elif second_exercise in lessons:
            lessons.remove(second_exercise)
            lessons.insert(lessons.index(title2) + 1, second_exercise)
        elif first_exercise in lessons and second_exercise in lessons:
            idx_first = lessons.index(first_exercise)
            idx_second = lessons.index(second_exercise)
            lessons[idx_first], lessons[idx_second] = lessons[idx_second], lessons[idx_first]
    return lessons


def exercise(title, lessons):
    if title in lessons and f"{title}-Exercise" not in lessons:
        needed_title_index = lessons.index(title)
        lessons.insert(needed_title_index + 1, f"{title}-Exercise")
    elif title not in lessons:
        lessons.append(title)
        lessons.append(f"{title}-Exercise")
    return lessons


current_lessons = input().split(", ")

while True:
    command1 = input()
    if command1 == "course start":
        break
    command = command1.split(":")
    if "Add" in command:
        current_title = command[1]
        add(current_title, current_lessons)
    elif "Insert" in command:
        current_title = command[1]
        current_idx = int(command[2])
        insert_el(current_title, current_idx, current_lessons)
    elif "Remove" in command:
        current_title = command[1]
        remove_el(current_title, current_lessons)
    elif "Swap" in command:
        current_title1 = command[1]
        current_title2 = command[2]
        swap_el(current_title1, current_title2, current_lessons)
    elif "Exercise" in command:
        current_title = command[1]
        exercise(current_title, current_lessons)

for i in range(1, len(current_lessons) + 1):
    print(f"{i}.{current_lessons[i - 1]}")