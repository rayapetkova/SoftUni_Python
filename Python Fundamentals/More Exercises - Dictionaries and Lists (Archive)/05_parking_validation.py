import re

num = int(input())
dictionary = {}
pattern = r"[A-Z]{2}\d{4}[A-Z]{2}"

for i in range(num):
    command = input().split()
    username = command[1]
    if "register" in command:
        license_plate_number = command[2]
        if username in dictionary.keys():
            print(f"ERROR: already registered with plate number {dictionary[username]}")
        elif not re.match(pattern, license_plate_number):
            print(f"ERROR: invalid license plate {license_plate_number}")
        elif license_plate_number in dictionary.values():
            print(f"ERROR: license plate {license_plate_number} is busy")
        else:
            dictionary[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif "unregister" in command:
        if username in dictionary.keys():
            print(f"user {username} unregistered successfully")
            del dictionary[username]
        else:
            print(f"ERROR: user {username} not found")

for key, value in dictionary.items():
    print(f"{key} => {value}")