type_flowers = input()
number_flowers = int(input())
budget = int(input())
all_price = 0

if type_flowers == "Roses":
    all_price = number_flowers * 5
    if number_flowers > 80:
        all_price = all_price - ((10 / 100) * all_price)
elif type_flowers == "Dahlias":
    all_price = number_flowers * 3.80
    if number_flowers > 90:
        all_price = all_price - ((15 / 100) * all_price)
elif type_flowers == "Tulips":
    all_price = number_flowers * 2.80
    if number_flowers > 80:
        all_price = all_price - ((15 / 100) * all_price)
elif type_flowers == "Narcissus":
    all_price = number_flowers * 3
    if number_flowers < 120:
        all_price = all_price + ((15 / 100) * all_price)
elif type_flowers == "Gladiolus":
    all_price = number_flowers * 2.50
    if number_flowers < 80:
        all_price = all_price + ((20 / 100) * all_price)

if budget >= all_price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {(budget - all_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(all_price - budget):.2f} leva more.")