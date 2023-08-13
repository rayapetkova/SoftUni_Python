nylon = int(input())
paint_in_L = int(input())
paint_thinner_in_L = int(input())
hours_needed = int(input())

nylon_sum = (nylon + 2) * 1.50
paint_in_L_sum = (paint_in_L + 0.1 * paint_in_L) * 14.50
paint_thinner_in_L_sum = paint_thinner_in_L * 5.00
bags = 0.40
material_sum = nylon_sum + paint_in_L_sum + paint_thinner_in_L_sum + bags
work = (30 / 100) * hours_needed * material_sum

total_sum = material_sum + work

print(f"{total_sum}")