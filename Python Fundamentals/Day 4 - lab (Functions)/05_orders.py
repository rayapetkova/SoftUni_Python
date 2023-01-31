

def total(purchase, times):
    if purchase == "coffee":
        return times * 1.50
    elif purchase == "coke":
        return times * 1.40
    elif purchase == "water":
        return times * 1.00
    elif purchase == "snacks":
        return times * 2.00


product = input()
quantity = int(input())
print(f"{total(product, quantity):.2f}")
