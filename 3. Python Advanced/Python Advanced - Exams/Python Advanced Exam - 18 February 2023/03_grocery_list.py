def shop_from_grocery_list(budget, *args):
    products_needed = args[0]
    bought = []
    for product, price in args[1:]:
        if product in bought:
            continue
        if product not in products_needed:
            continue
        if budget >= price:
            budget -= price
            bought.append(product)
            products_needed.remove(product)
        else:
            break
    if not products_needed:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(products_needed)}."


# Test inputs:

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
