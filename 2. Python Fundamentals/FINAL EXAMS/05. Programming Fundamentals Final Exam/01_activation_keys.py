text = input()

while True:
    line = input()
    if line == "Generate":
        break
    command = line.split(">>>")
    if "Contains" in command:
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print(f"Substring not found!")
    elif "Flip" in command:
        start, end = int(command[2]), int(command[3])
        if "Upper" in command:
            text = text[:start] + text[start:end].upper() + text[end:]
        else:
            text = text[:start] + text[start:end].lower() + text[end:]
        print(text)
    elif "Slice" in command:
        start, end = int(command[1]), int(command[2])
        text = text[:start] + text[end:]
        print(text)

print(f"Your activation key is: {text}")