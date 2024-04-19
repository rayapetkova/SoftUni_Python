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
        bill = bill - 5  # bill -= 5

    left_seats = cinema_capacity - people
    if left_seats < 0:
        print(f"The cinema is full.")
        break
    else:
        total_income = total_income + bill  # total_income += bill
        cinema_capacity = cinema_capacity - people

    input_line = input()

print(f"Cinema income - {total_income} lv.")