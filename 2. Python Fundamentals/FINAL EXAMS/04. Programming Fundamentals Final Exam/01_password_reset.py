password = input()

while True:
    line = input()
    if line == "Done":
        break
    if line == "TakeOdd":
        password = password[1::2]
        print(password)
    command = line.split()
    if "Cut" in command:
        idx, length = int(command[1]), int(command[2])
        password = password[:idx] + password[idx + length :]
        print(password)
    elif "Substitute" in command:
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")

print(f"Your password is: {password}")