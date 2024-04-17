cinema_capacity = int(input())
total_income = 0

input_line = input()
while input_line:
    if input_line == "Movie time!":
        print(f"There are {cinema_capacity} seats left in the cinema.")
        break

    people = int(input_line)
    bill = people * 5

    if people % 3 == 0:
        bill -= 5

    if cinema_capacity - people < 0:
        print(f"The cinema is full.")
        break
    else:
        total_income += bill
        cinema_capacity -= people

    input_line = input()

print(f"Cinema income - {total_income} lv.")