dictionary = {}

while True:
    line = input()
    if line == "login":
        break
    username, password = line.split(" -> ")
    dictionary[username] = password

unsuccessful = 0
while True:
    line = input()
    if line == "end":
        break
    username, password = line.split(" -> ")
    if username not in dictionary.keys() or dictionary[username] != password:
        print(f"{username}: login failed")
        unsuccessful += 1
    else:
        print(f"{username}: logged in successfully")

print(f"unsuccessful login attempts: {unsuccessful}")