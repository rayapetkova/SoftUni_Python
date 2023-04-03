text = input()

while True:
    line = input()
    if line == "Decode":
        break
    command = line.split("|")
    if "Move" in command:
        number = int(command[1])
        first_n_letters = text[0:number]
        text = text.replace(text[0:number], "")
        text += first_n_letters
    elif "Insert" in command:
        idx = int(command[1])
        value = command[2]
        text = text[0:idx] + value + text[idx:]
    elif "ChangeAll" in command:
        substring = command[1]
        replacement = command[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")