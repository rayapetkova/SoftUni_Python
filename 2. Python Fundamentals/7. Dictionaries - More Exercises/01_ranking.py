first_dictionary = {}
second_dictionary = {}

while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    first_dictionary[contest] = password

while True:
    line = input()
    if line == "end of submissions":
        break
    command = line.split("=>")
    person_contest, person_password, username, points = command[0], command[1], command[2], int(command[3])
    if person_contest in first_dictionary.keys():
        if first_dictionary[person_contest] == person_password:
            second_dictionary[username] = second_dictionary.get(username, {})
            # The get method can be replaced with this:
            # if person_contest not in second_dictionary[username]:
            #     second_dictionary[username][person_contest] = 0
            second_dictionary[username][person_contest] = second_dictionary[username].get(person_contest, 0)
            if points > second_dictionary[username][person_contest]:
                second_dictionary[username][person_contest] = points

all_results = {}
total = 0

for key, value in second_dictionary.items():
    for second_key, second_value in value.items():
        total = sum(value.values())
    all_results[key] = total

max_score = max(all_results.values())
needed_person = ''
for name, score in all_results.items():
    if score == max_score:
        needed_person = name
        break
print(f"Best candidate is {needed_person} with total {max_score} points.")

print(f"Ranking:")
for final_name, final_score in sorted(second_dictionary.items()):
    print(final_name)
    second_dict_values = second_dictionary[final_name]
    for course_name, course_points in sorted(second_dict_values.items(), key=lambda kv: kv[1], reverse=True):
        print(f"#  {course_name} -> {course_points}")