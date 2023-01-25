start_sum = int(input())

counter = 0
sum_products = 0
counter_card = 0
counter_cash = 0
card_sum = 0
cash_sum = 0
all_price = 0
over = False

while True:
    product_price = input()
    if product_price == "End":
        print("Failed to collect required money for charity.")
        break
    elif product_price != "End":
        product_price = int(product_price)
        counter = counter + 1
        if counter % 2 == 0:
            if product_price >= 10:
                counter_card = counter_card + 1
                print("Product sold!")
                card_sum = card_sum + product_price
                all_price = all_price + product_price
            else:
                print("Error in transaction!")
        else:
            if product_price <= 100:
                counter_cash = counter_cash + 1
                print("Product sold!")
                cash_sum = cash_sum + product_price
                all_price = all_price + product_price
            else:
                print("Error in transaction!")

        if all_price >= start_sum:
            over = True
            break

if over:
    print(f"Average CS: {(cash_sum / counter_cash):.2f}")
    print(f"Average CC: {(card_sum / counter_card):.2f}")