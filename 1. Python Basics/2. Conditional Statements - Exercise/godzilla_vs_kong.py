movie_budget = float(input())
actors_num = int(input())
one_suit_price = float(input())

decor = (10 / 100) * movie_budget
all_suits_price = one_suit_price * actors_num

if actors_num >= 150:
    suits_with_discount = all_suits_price - ((10 / 100) * all_suits_price)
    all_sum = decor + suits_with_discount
else:
    all_sum = decor + all_suits_price

if all_sum > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(all_sum - movie_budget):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {(movie_budget - all_sum):.2f} leva left.")
