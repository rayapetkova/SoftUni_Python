products = input().split()
dictionary = {}

for i in range(0, len(products), 2):
    product = products[i]
    quantity = int(products[i + 1])
    dictionary[product] = quantity

print(dictionary)