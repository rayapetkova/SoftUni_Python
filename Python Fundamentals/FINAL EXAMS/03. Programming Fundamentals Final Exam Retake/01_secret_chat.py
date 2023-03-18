message = input()

while True:
    line = input()
    if line == "Reveal":
        break
    command = line.split(":|:")
    if "InsertSpace" in command:
        idx = int(command[1])
        message = message[:idx] + " " + message[idx:]
        print(message)
    elif "Reverse" in command:
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            new_message = substring[::-1]
            message += new_message
            print(message)
        else:
            print("error")
    elif "ChangeAll" in command:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")