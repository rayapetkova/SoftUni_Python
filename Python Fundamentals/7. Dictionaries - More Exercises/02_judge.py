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
    contest_dict[contest] = contest_dict.get(contest, {})
    contest_dict[contest][username] = contest_dict[contest].get(username, 0)
    if points > contest_dict[contest][username]:
        contest_dict[contest][username] = points

    individual_standings[username] = individual_standings.get(username, {})
    individual_standings[username][contest] = individual_standings[username].get(contest, 0)
    if points > individual_standings[username][contest]:
        individual_standings[username][contest] = points

for name in contest_dict.keys():
    second_dict_values = contest_dict[name]
    print(f"{name}: {len(second_dict_values)} participants")
    for pos, (key, value) in enumerate(sorted(second_dict_values.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {key} <::> {value}")

new_dictionary = {}

for individual_name in individual_standings.keys():
    second_dict = individual_standings[individual_name]
    sum_points = sum(second_dict.values())
    new_dictionary[individual_name] = sum_points

print(f"Individual standings:")
el1 = 1
for position, (key, value) in enumerate(sorted(new_dictionary.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {key} -> {value}")
