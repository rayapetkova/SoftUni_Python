number = int(input())
dictionary = {}

for _ in range(number):
    command = input().split()
    username = command[1]
    if "register" in command:
        license_number = command[2]
        if username not in dictionary.keys():
            dictionary[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif "unregister" in command:
        if username not in dictionary.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del dictionary[username]

for key, value in dictionary.items():
    print(f"{key} => {value}")