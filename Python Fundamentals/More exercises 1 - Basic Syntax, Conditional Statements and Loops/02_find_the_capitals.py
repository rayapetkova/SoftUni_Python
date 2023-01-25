string_given = input()
output = []

for i in range(len(string_given)):
    if string_given[i].isupper():
        output.append(i)

print(output)