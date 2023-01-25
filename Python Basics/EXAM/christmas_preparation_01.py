wrapping_paper_num = int(input())
cloth_num = int(input())
glue_L = float(input())
discount_in_percents = int(input())

wrapping_paper_price = wrapping_paper_num * 5.80
cloth_price = cloth_num * 7.20
glue_price = glue_L * 1.20
total_price = wrapping_paper_price + cloth_price + glue_price

total_price_with_discount = total_price - ((discount_in_percents / 100) * total_price)
print(f"{total_price_with_discount:.3f}")