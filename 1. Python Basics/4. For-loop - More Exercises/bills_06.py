months = int(input())

electricity_bill = 0
water_bill = 0
internet_bill = 0
electricity_bill_for_month = 0
others = 0

for i in range(1, months + 1):
    electricity_bill_for_month = float(input())
    electricity_bill = electricity_bill + electricity_bill_for_month
    water_bill = months * 20
    internet_bill = months * 15
    others = others + (electricity_bill_for_month + 20 + 15) + 20 / 100 * (electricity_bill_for_month + 20 + 15)

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others:.2f} lv")

average_total_sum = (electricity_bill + water_bill + internet_bill + others) / months
print(f"Average: {average_total_sum:.2f} lv")