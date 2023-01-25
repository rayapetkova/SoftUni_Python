number = int(input())
sum_numbers = 1

while sum_numbers <= number:
    print(sum_numbers)
    sum_numbers = sum_numbers * 2 + 1

    if sum_numbers > number:
        break