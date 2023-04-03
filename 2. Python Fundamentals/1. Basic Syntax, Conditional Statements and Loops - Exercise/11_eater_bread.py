budget = float(input())
price_1kg_flour = float(input())
price_one_pack_of_eggs = (75 / 100) * price_1kg_flour
price_one_L_milk = price_1kg_flour + (25 / 100) * price_1kg_flour
price_for_250_ml_milk = price_one_L_milk / 4

one_loaf_price = price_1kg_flour + price_one_pack_of_eggs + price_for_250_ml_milk
loaves_counter = 0
coloured_eggs = 0

while True:
    if budget < one_loaf_price:
        break
    else:
        budget = budget - one_loaf_price
    loaves_counter = loaves_counter + 1
    coloured_eggs = coloured_eggs + 3

    if loaves_counter % 3 == 0:
        coloured_eggs = coloured_eggs - (loaves_counter - 2)

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")