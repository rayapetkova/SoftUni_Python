age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input())

count_toys = 0
money = 0
total_sum = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money = money + 10
        total_sum = (total_sum + money) - 1
    else:
        count_toys = count_toys + 1

all_price = (count_toys * one_toy_price) + total_sum

if all_price >= washing_machine_price:
    print(f"Yes! {(all_price - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - all_price):.2f}")