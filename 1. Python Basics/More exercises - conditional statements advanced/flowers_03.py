chr_num = int(input())
roses_num = int(input())
tulips_num = int(input())
season = input()
holiday = input()

chr_price = 0
roses_price = 0
tulips_price = 0
total_price = 0
all_flowers = chr_num + roses_num + tulips_num

if season == "Spring" or season == "Summer":
    chr_price = chr_num * 2.00
    roses_price = roses_num * 4.10
    tulips_price = tulips_num * 2.50
    total_price = chr_price + roses_price + tulips_price
elif season == "Autumn" or season == "Winter":
    chr_price = chr_num * 3.75
    roses_price = roses_num * 4.50
    tulips_price = tulips_num * 4.15
    total_price = chr_price + roses_price + tulips_price

if holiday == "Y":
    total_price = total_price + ((15 / 100) * total_price)
elif holiday == "N":
    total_price = chr_price + roses_price + tulips_price

if season == "Spring" and tulips_num > 7:
    total_price = total_price - ((5 / 100) * total_price)
if season == "Winter" and roses_num >= 10:
    total_price = total_price - ((10 / 100) * total_price)
if all_flowers > 20:
    total_price = total_price - ((20 / 100) * total_price)

print(f"{(total_price + 2):.2f}")