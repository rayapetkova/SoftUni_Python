dictionary = {}
count_unliked_meals = 0

while True:
    line = input()
    if line == "Stop":
        break
    command = line.split("-")
    guest, meal = command[1], command[2]
    if "Like" in command:
        dictionary[guest] = dictionary.get(guest, [])
        if meal not in dictionary[guest]:
            dictionary[guest].append(meal)
    elif "Dislike" in command:
        if guest in dictionary.keys():
            if meal in dictionary[guest]:
                print(f"{guest} doesn't like the {meal}.")
                dictionary[guest] = [something for something in dictionary[guest] if something != meal]
                count_unliked_meals += 1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

for key, value in dictionary.items():
    if not value:
        print(f"{key}: ")
    if value:
        print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {count_unliked_meals}")