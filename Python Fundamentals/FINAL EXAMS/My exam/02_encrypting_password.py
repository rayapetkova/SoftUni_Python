import re

num = int(input())

pattern = r"(.+)>(?P<password>\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1"

for i in range(num):
    line = input()
    valid_passwords = re.finditer(pattern, line)
    final = []
    for valid in valid_passwords:
        final.append(valid.group('password'))
    if final:
        second = ""
        for some in final:
            second = some.replace("|", "")
        print(f"Password: {second}")
    else:
        print(f"Try another password!")
