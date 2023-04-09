first = set(int(n) for n in input().split())
second = set(int(n) for n in input().split())
num = int(input())

for i in range(num):
    line = input().split()
    if line[0] == "Add" and line[1] == "First":
        for el in line:
            if el.isdigit():
                first.add(int(el))
    elif line[0] == "Add" and line[1] == "Second":
        for el in line:
            if el.isdigit():
                second.add(int(el))
    elif line[0] == "Remove" and line[1] == "First":
        for el in line:
            if el.isdigit():
                first.discard(int(el))
    elif line[0] == "Remove" and line[1] == "Second":
        for el in line:
            if el.isdigit():
                second.discard(int(el))
    elif "Check" in line:
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(', '.join(str(n) for n in sorted(first)))
print(', '.join(str(n) for n in sorted(second)))
