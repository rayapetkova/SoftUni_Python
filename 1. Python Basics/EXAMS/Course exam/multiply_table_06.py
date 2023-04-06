number = int(input())

number = str(number)
first_number = number[2]
first_number = int(first_number)

second_number = number[1]
second_number = int(second_number)

third_number = number[0]
third_number = int(third_number)

for i in range(1, first_number + 1):
    for j in range(1, second_number + 1):
        for k in range(1, third_number + 1):
            print(f"{i} * {j} * {k} = {i * j * k};")