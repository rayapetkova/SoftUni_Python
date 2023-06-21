num = int(input())
dictionary = {}

for i in range(num):
    command = input().split()
    name, grade = command[0], float(command[1])
    dictionary[name] = dictionary.get(name, []) + [grade]

for student, grades in dictionary.items():
    print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {(sum(grades) / len(grades)):.2f})")
