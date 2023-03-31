from math import ceil

dictionary = {}

while True:
    line = input()
    if line == "Aggregate":
        break
    command = line.split()
    name, size = command[0], int(command[1])
    dictionary[name] = dictionary.get(name, []) + [size]

for key, value in dictionary.items():
    result = []
    [result.append(element) for element in value if element not in result]
    giant_shell_size = ceil(sum(result) - (sum(result) / len(result)))
    print(f"{key} -> {', '.join([str(el) for el in result])} ({giant_shell_size})")