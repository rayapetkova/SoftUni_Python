juniors_num = int(input())
seniors_num = int(input())
track = input()
all_price = 0

if track == "trail":
    juniors_all_price = juniors_num * 5.50
    seniors_all_price = seniors_num * 7
    all_price = juniors_all_price + seniors_all_price
    all_price = all_price - ((5 / 100) * all_price)
elif track == "cross-country":
    juniors_all_price = juniors_num * 8
    seniors_all_price = seniors_num * 9.50
    all_price = juniors_all_price + seniors_all_price
    if juniors_num + seniors_num >= 50:
        all_price = all_price - ((25 / 100) * all_price)
        all_price = all_price - ((5 / 100) * all_price)
    else:
        all_price = juniors_all_price + seniors_all_price
        all_price = all_price - ((5 / 100) * all_price)
elif track == "downhill":
    juniors_all_price = juniors_num * 12.25
    seniors_all_price = seniors_num * 13.75
    all_price = juniors_all_price + seniors_all_price
    all_price = all_price - ((5 / 100) * all_price)
elif track == "road":
    juniors_all_price = juniors_num * 20
    seniors_all_price = seniors_num * 21.50
    all_price = juniors_all_price + seniors_all_price
    all_price = all_price - ((5 / 100) * all_price)

print(f"{all_price:.2f}")