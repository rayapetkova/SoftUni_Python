pens_num = int(input())
markers_num = int(input())
board_cleaner_in_L = int(input())
discount_percentage = int(input())

pens_price = pens_num * 5.80
markers_price = markers_num * 7.20
board_cleaner_price = board_cleaner_in_L * 1.20
discount = (pens_price + markers_price + board_cleaner_price) * (discount_percentage / 100)

total_price = (pens_price + markers_price + board_cleaner_price) - discount

print(total_price)