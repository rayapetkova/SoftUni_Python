dictionary = {}
languages = {}

while True:
    line = input()
    if line == "exam finished":
        break
    command = line.split("-")
    if len(command) == 3:
        username, language, points = command[0], command[1], int(command[2])
        languages[language] = languages.get(language, 0) + 1
        if username in dictionary.keys():
            if points > dictionary[username]:
                dictionary[username] = points
        else:
            dictionary[username] = points
    else:
        dictionary[command[0]] = 0

print(f"Results:")
[print(f"{key} | {value}") for key, value in dictionary.items() if value != 0]

print(f"Submissions:")
[print(f"{some_language} - {number}") for some_language, number in languages.items()]