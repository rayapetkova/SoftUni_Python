num = int(input())
dictionary = {}

for i in range(num):
    piece, composer, key = input().split("|")
    dictionary[piece] = dictionary.get(piece, {"composer": None, "key": None})
    dictionary[piece]["composer"] = composer
    dictionary[piece]["key"] = key

while True:
    line = input()
    if line == "Stop":
        break
    command = line.split("|")
    piece = command[1]
    if "Add" in line:
        composer, key = command[2], command[3]
        if piece in dictionary.keys():
            print(f"{piece} is already in the collection!")
        else:
            dictionary[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif "Remove" in line:
        if piece not in dictionary.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del dictionary[piece]
            print(f"Successfully removed {piece}!")
    elif "ChangeKey" in line:
        new_key = command[2]
        if piece in dictionary.keys():
            dictionary[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in dictionary.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")