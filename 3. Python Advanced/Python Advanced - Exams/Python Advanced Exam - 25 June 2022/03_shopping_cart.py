def shopping_cart(*args):
    dictionary = {'Soup': [], 'Pizza': [], 'Dessert': []}
    final_print = []
    for element in args:
        if element == "Stop":
            break
        type_meal, product = element
        if type_meal == "Soup" and len(dictionary['Soup']) < 3 and product not in dictionary['Soup']:
            dictionary['Soup'].append(product)
        elif type_meal == "Pizza" and len(dictionary['Pizza']) < 4 and product not in dictionary['Pizza']:
            dictionary['Pizza'].append(product)
        elif type_meal == "Dessert" and len(dictionary['Dessert']) < 2 and product not in dictionary['Dessert']:
            dictionary['Dessert'].append(product)
    sorted_dict = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_dict:
        sorted_products = sorted(value)
        final_print.append(f"{key}:")
        for some_product in sorted_products:
            final_print.append(f" - {some_product}")
    if len(final_print) > 3:
        return '\n'.join(final_print)
    return f"No products in the cart!"


# Test inputs:

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))


# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
