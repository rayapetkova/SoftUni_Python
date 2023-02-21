dictionary = {}
line = input()

while not line.isdigit():
    name, phone_numbers = line.split("-")
    dictionary[name] = phone_numbers
    line = input()

for i in range(int(line)):
    some_name = input()
    if some_name not in dictionary.keys():
        print(f"Contact {some_name} does not exist.")
    else:
        print(f"{some_name} -> {dictionary[some_name]}")