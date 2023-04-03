products = input().split()
checking_products = input().split()
dictionary = {}

for i in range(0, len(products), 2):
    product = products[i]
    quantity = products[i + 1]
    dictionary[product] = quantity

for j in checking_products:
    if j in dictionary.keys():
        print(f"We have {dictionary[j]} of {j} left")
    else:
        print(f"Sorry, we don't have {j}")