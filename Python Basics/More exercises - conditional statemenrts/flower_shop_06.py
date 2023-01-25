from math import floor, ceil

magnolias_num = int(input())
hyacinths_num = int(input())
roses_num = int(input())
cacti_num = int(input())
present_price = float(input())

all_magnolias_price = magnolias_num * 3.25
all_hyacinths_price = hyacinths_num * 4
all_roses_price = roses_num * 3.50
all_cacti_price = cacti_num * 8
price = all_magnolias_price + all_hyacinths_price + all_roses_price + all_cacti_price
all_price = price - ((5 / 100) * price)

if all_price >= present_price:
    print(f"She is left with {floor(all_price - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - all_price)} leva.")