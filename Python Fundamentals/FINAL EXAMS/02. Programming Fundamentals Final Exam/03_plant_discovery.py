num = int(input())

dictionary = {}

for i in range(num):
    line = input().split("<->")
    curr_plant, curr_rarity = line[0], int(line[1])
    dictionary[curr_plant] = dictionary.get(curr_plant, {'rarity': 0, 'rating': []})
    dictionary[curr_plant]['rarity'] += curr_rarity

while True:
    line = input()
    if line == "Exhibition":
        break
    command = line.split(": ")
    new = command[1].split(" - ")
    plant = new[0]
    if "Rate" in command:
        rating = int(new[1])
        if plant in dictionary.keys():
            dictionary[plant]['rating'].append(rating)
        else:
            print("error")
    elif "Update" in command:
        new_rarity = int(new[1])
        if plant in dictionary.keys():
            dictionary[plant]['rarity'] = new_rarity
        else:
            print(f"error")
    elif "Reset" in command:
        if plant in dictionary.keys():
            dictionary[plant]['rating'] = []
        else:
            print("error")

print(f"Plants for the exhibition:")
for key, value in dictionary.items():
    result = 0
    if not value['rating']:
        result = 0
    else:
        result = sum(value['rating']) / len(value['rating'])
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {result:.2f}")