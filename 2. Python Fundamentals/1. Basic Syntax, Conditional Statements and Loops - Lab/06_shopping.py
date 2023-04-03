budget = int(input())
total = 0

while True:
    product_price = input()

    if product_price == "End":
        print("You bought everything needed.")
        break
    else:
        product_price = int(product_price)
        total = total + product_price
        if total > budget:
            print("You went in overdraft!")
            break