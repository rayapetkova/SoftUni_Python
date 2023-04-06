one_lv_coins_num = int(input())
two_lv_coins_num = int(input())
five_lv_num = int(input())
needed_sum = int(input())

for i in range(0, one_lv_coins_num + 1):
    for j in range(0, two_lv_coins_num + 1):
        for k in range(0, five_lv_num + 1):
            total = i * 1 + j * 2 + k * 5
            if total == needed_sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {needed_sum} lv.")