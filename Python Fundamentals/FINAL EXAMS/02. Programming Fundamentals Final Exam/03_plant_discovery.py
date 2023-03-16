n = int(input())
dictionary = {}

for i in range(n):
    plant, rarity = input().split("<->")
    dictionary[plant] = dictionary.get(plant, {"rarity": None, "ratings": []})
    dictionary[plant]["rarity"] = rarity

while True:
    line = input()
    if line == "Exhibition":
        break
    line = line.split(": ")
    if "Rate" in line:
        command = line[1].split(" - ")
        some_plant, rating = command[0], float(command[1])
        if some_plant in dictionary.keys():
            dictionary[some_plant]["ratings"].append(rating)
        else:
            print("error")
    elif "Update" in line:
        command = line[1].split(" - ")
        some_plant, new_rarity = command[0], float(command[1])
        if some_plant in dictionary.keys():
            dictionary[some_plant]["rarity"] = new_rarity
        else:
            print("error")
    elif "Reset" in line:
        some_plant = line[1]
        if some_plant in dictionary.keys():
            del dictionary[some_plant]["ratings"][0:]
        else:
            print("error")

final_ratings = 0
print(f"Plants for the exhibition:")
for key, value in dictionary.items():
    if len(value['ratings']) == 0:
        final_ratings = 0
    else:
        final_ratings = sum(value['ratings']) / len(value['ratings'])
    print(f"- {key}; Rarity: {int(value['rarity'])}; Rating: {final_ratings:.2f}")