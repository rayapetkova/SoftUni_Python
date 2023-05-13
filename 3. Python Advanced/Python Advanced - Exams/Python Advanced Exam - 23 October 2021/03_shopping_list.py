def shopping_list(budget, **kwargs):
    basket, final_output = 0, []

    if budget < 100:
        return f"You do not have enough budget."

    for product, value in kwargs.items():
        if basket == 5:
            break

        total_price = float(value[0]) * int(value[1])
        if budget < total_price:
            continue

        basket += 1
        budget -= total_price
        final_output.append(f"You bought {product} for {total_price:.2f} leva.")

    return "\n".join(final_output)


# Test inputs:

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
