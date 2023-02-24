dictionary = {}

while True:
    line = input()
    if line == "statistics":
        break
    product, quantity = line.split(": ")

    if product not in dictionary.keys():
        dictionary[product] = int(quantity)
    else:
        dictionary[product] += int(quantity)

print(f"Products in stock:")

[print(f"- {key}: {value}") for key, value in dictionary.items()]

print(f"Total Products: {len(dictionary.keys())}")
print(f"Total Quantity: {sum(dictionary.values())}")





#2
#
# dictionary = {}
#
# while True:
#     line = input()
#     if line == "statistics":
#         break
#     product, quantity = line.split(": ")
#
#     if product not in dictionary:
#         dictionary[product] = 0
#
#     dictionary[product] += int(quantity)
#
# print(f"Products in stock:")
#
# [print(f"- {key}: {value}") for key, value in dictionary.items()]
#
# print(f"Total Products: {len(dictionary.keys())}")
# print(f"Total Quantity: {sum(dictionary.values())}")
