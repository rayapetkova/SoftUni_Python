moves = int(input())

result = 0
first_numbers = 0
second_numbers = 0
third_numbers = 0
fourth_numbers = 0
fifth_numbers = 0
invalid_numbers = 0

for i in range(1, moves + 1):
    new_number = int(input())
    if 0 <= new_number <= 9:
        result = result + ((20 / 100) * new_number)
        first_numbers = first_numbers + 1
    elif 10 <= new_number <= 19:
        result = result + ((30 / 100) * new_number)
        second_numbers = second_numbers + 1
    elif 20 <= new_number <= 29:
        result = result + ((40 / 100) * new_number)
        third_numbers = third_numbers + 1
    elif 30 <= new_number <= 39:
        result = result + 50
        fourth_numbers = fourth_numbers + 1
    elif 40 <= new_number <= 50:
        result = result + 100
        fifth_numbers = fifth_numbers + 1
    elif new_number < 0 or new_number > 50:
        result = result / 2
        invalid_numbers = invalid_numbers + 1

print(f"{result:.2f}")

all_numbers = first_numbers + second_numbers + third_numbers + fourth_numbers + fifth_numbers + invalid_numbers

first_numbers_percents = (first_numbers / all_numbers) * 100
print(f"From 0 to 9: {first_numbers_percents:.2f}%")

second_numbers_percents = (second_numbers / all_numbers) * 100
print(f"From 10 to 19: {second_numbers_percents:.2f}%")

third_numbers_percents = (third_numbers / all_numbers) * 100
print(f"From 20 to 29: {third_numbers_percents:.2f}%")

fourth_numbers_percents = (fourth_numbers / all_numbers) * 100
print(f"From 30 to 39: {fourth_numbers_percents:.2f}%")

fifth_numbers_percents = (fifth_numbers / all_numbers) * 100
print(f"From 40 to 50: {fifth_numbers_percents:.2f}%")

invalid_numbers_percents = (invalid_numbers / all_numbers) * 100
print(f"Invalid numbers: {invalid_numbers_percents:.2f}%")