contest_dict = {}
# {Python: {Katie: 200}}
individual_standings = {}
# {Katie: {'Python': 200, 'JS': 200}}

while True:
    line = input()
    if line == "no more time":
        break
    command = line.split(" -> ")
    username, contest, points = command[0], command[1], int(command[2])
    if contest in contest_dict.keys():
        if username in contest_dict[contest]:
            if points > contest_dict[contest][username]:
                contest_dict[contest][username] = points
        else:
            contest_dict[contest][username] = contest_dict[contest].get(username, points)
    else:
        contest_dict[contest] = contest_dict.get(contest, {})
        contest_dict[contest][username] = contest_dict[contest].get(username, points)

    if username in individual_standings.keys():
        if contest in individual_standings[username]:
            if points > individual_standings[username][contest]:
                individual_standings[username][contest] = points
        else:
            individual_standings[username][contest] = individual_standings[username].get(contest, points)
    else:
        individual_standings[username] = individual_standings.get(username, {})
        individual_standings[username][contest] = individual_standings[username].get(contest, points)

for name in contest_dict.keys():
    second_dict_values = contest_dict[name]
    print(f"{name}: {len(second_dict_values)} participants")
    el = 1
    for key, value in sorted(second_dict_values.items(), key=lambda x: (-x[1], x[0])):
        for num in range(el, len(second_dict_values) + 1):
            print(f"{num}. {key} <::> {value}")
            el += 1
            break

new_dictionary = {}

for individual_name in individual_standings.keys():
    second_dict = individual_standings[individual_name]
    sum_points = sum(second_dict.values())
    new_dictionary[individual_name] = sum_points

print(f"Individual standings:")
el1 = 1
for key, value in sorted(new_dictionary.items(), key=lambda x: (-x[1], x[0])):
    for n in range(el1, len(new_dictionary) + 1):
        print(f"{n}. {key} -> {value}")
        el1 += 1
        break
