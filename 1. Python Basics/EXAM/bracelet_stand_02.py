pocket_money = float(input())
money_day_from_sells = float(input())
expenses = float(input())
present_price = float(input())

money_from_pocket_money = pocket_money * 5
won_money = money_day_from_sells * 5
total = money_from_pocket_money + won_money
total_without_expenses = total - expenses

if total_without_expenses >= present_price:
    print(f"Profit: {total_without_expenses:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(present_price - total_without_expenses):.2f} BGN.")