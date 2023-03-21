dictionary = {}

while True:
    line = input()
    if line == "Sail":
        break
    command = line.split("||")
    city, population, curr_gold = command[0], int(command[1]), int(command[2])
    dictionary[city] = dictionary.get(city, {'population': 0, 'gold': 0})
    dictionary[city]['population'] += population
    dictionary[city]['gold'] += curr_gold

while True:
    line = input()
    if line == "End":
        break
    command = line.split("=>")
    town = command[1]
    if "Plunder" in command:
        people, gold = int(command[2]), int(command[3])
        dictionary[town]['population'] -= people
        dictionary[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if dictionary[town]['population'] <= 0 or dictionary[town]['gold'] <= 0:
            del dictionary[town]
            print(f"{town} has been wiped off the map!")
    elif "Prosper" in command:
        gold = int(command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        dictionary[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town]['gold']} gold.")

if not dictionary:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
    exit()
print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
for key, value in dictionary.items():
    print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
