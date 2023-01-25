greening_meters = float(input())

price = greening_meters * 7.61
discount = price * 0.18
final_price = price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")