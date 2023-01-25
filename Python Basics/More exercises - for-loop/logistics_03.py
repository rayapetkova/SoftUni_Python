loads_num = int(input())

total_price_van = 0
total_price_truck = 0
total_price_train = 0
tons_sum_van = 0
tons_sum_truck = 0
tons_sum_train = 0
tons_sum = 0

for i in range(1, loads_num + 1):
    tons = int(input())
    if tons <= 3:
        total_price_van = total_price_van + 200 * tons
        tons_sum = tons_sum + tons
        tons_sum_van = tons_sum_van + tons
    elif 4 <= tons <= 11:
        total_price_truck = total_price_truck + 175 * tons
        tons_sum = tons_sum + tons
        tons_sum_truck = tons_sum_truck + tons
    elif tons >= 12:
        total_price_train = total_price_train + 120 * tons
        tons_sum = tons_sum + tons
        tons_sum_train = tons_sum_train + tons


average_price = (total_price_van + total_price_truck + total_price_train) / tons_sum
print(f"{average_price:.2f}")

percents_van = (tons_sum_van / tons_sum) * 100
print(f"{percents_van:.2f}%")

percents_truck = (tons_sum_truck / tons_sum) * 100
print(f"{percents_truck:.2f}%")

percents_train = (tons_sum_train / tons_sum) * 100
print(f"{percents_train:.2f}%")