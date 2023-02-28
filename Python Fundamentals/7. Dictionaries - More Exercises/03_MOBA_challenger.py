# We are creating a dictionary named "pool", which will look like this:
# {player: {position: skill}}
# Example: {"George": {Jungle: 250}}
pool = {}

# "final" is the second dictionary, in which we are going to keep the names of the players and their total skill:
# Simon: 450 skill
# {player: total_skill}
# Example: {"Simon": 450, "Frank": 350, "Peter": 200}
final = {}

while True:
    line = input()
    if line == "Season end":
        break
    if "->" in line:
        player, position, skill = [int(element) if element.isdigit() else element for element in line.split(" -> ")]
        if player not in pool.keys():
            pool[player] = {position: skill}
        else:
            if position in pool[player]:
                if skill > pool[player][position]:
                    pool[player][position] = skill
            else:
                pool[player] = pool.get(player, {})
                pool[player][position] = pool[player].get(position, skill)
    else:
        command = line.split(" vs ")
        first_player, second_player = command[0], command[1]
        if first_player in pool.keys() and second_player in pool.keys():
            for first in pool[first_player].keys():
                for second in pool[second_player].keys():
                    if first == second:
                        if pool[first_player][first] > pool[second_player][second]:
                            pool[second_player][second] = 0
                        elif pool[second_player][second] > pool[first_player][first]:
                            pool[first_player][first] = 0

for key, value in pool.items():
    final[key] = sum(value.values())

for name, total in sorted(final.items(), key=lambda x: (-x[1], x[0])):
    if total != 0:
        print(f"{name}: {total} skill")
        for second_key, second_value in sorted(pool[name].items(), key=lambda x: (-x[1], x[0])):
            print(f"- {second_key} <::> {second_value}")