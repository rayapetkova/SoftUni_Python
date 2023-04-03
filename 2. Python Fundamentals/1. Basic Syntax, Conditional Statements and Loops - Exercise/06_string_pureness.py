n = int(input())

for i in range(1, n + 1):
    string_given = input()
    if "," in string_given:
        print(f"{string_given} is not pure!")
    elif "." in string_given:
        print(f"{string_given} is not pure!")
    elif "_" in string_given:
        print(f"{string_given} is not pure!")
    else:
        print(f"{string_given} is pure.")