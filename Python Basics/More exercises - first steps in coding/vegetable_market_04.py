vegetables_one_kg = float(input())
fruits_one_kg = float(input())
vegetables_all_kg = int(input())
fruits_all_kg = int(input())

vegetables = vegetables_one_kg * vegetables_all_kg
fruits = fruits_one_kg * fruits_all_kg
total_sum_in_euro = (vegetables + fruits) / 1.94

print(f"{total_sum_in_euro:.2f}")