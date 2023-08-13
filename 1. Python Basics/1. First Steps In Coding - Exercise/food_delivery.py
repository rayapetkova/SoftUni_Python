meat_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

meat_menus_price = meat_menus * 10.35
fish_menus_price = fish_menus * 12.40
vegetarian_menus_price = vegetarian_menus * 8.15
all_menus_price = meat_menus_price + fish_menus_price + vegetarian_menus_price
dessert = (20 / 100) * all_menus_price
delivery = 2.50

total_price = all_menus_price + dessert + delivery

print(total_price)