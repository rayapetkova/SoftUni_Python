budget = float(input())
video_cards_num = int(input())
processors_num = int(input())
ram_memory_num = int(input())

all_video_cards_price = video_cards_num * 250
all_processors_price = processors_num * ((35 / 100) * all_video_cards_price)
all_ram_memory_price = ram_memory_num * ((10 / 100) * all_video_cards_price)
all_sum = all_video_cards_price + all_processors_price + all_ram_memory_price

if video_cards_num > processors_num:
    all_sum = all_sum - ((15 / 100) * all_sum)

if budget >= all_sum:
    print(f"You have {(budget - all_sum):.2f} leva left!")
else:
    print(f"Not enough money! You need {(all_sum - budget):.2f} leva more!")
