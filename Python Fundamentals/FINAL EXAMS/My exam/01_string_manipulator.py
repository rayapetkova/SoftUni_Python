text = input()

while True:
    line = input()
    if line == "End":
        break
    command = line.split()
    if "Translate" in command:
        character, replacement = command[1], command[2]
        text = text.replace(character, replacement)
        print(text)
    elif "Includes" in command:
        substring = command[1]
        if substring in text:
            print("True")
        else:
            print(f"False")
    elif "Start" in command:
        substring = command[1]
        check_if = text.startswith(substring)
        print(check_if)
    elif "Lowercase" in command:
        text = text.lower()
        print(text)
    elif "FindIndex" in command:
        character = command[1]
        print(text.rfind(character))
    elif "Remove" in command:
        start, count = int(command[1]), int(command[2])
        text = text[:start] + text[start + count:]
        print(text)