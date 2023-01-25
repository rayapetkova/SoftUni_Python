year_tax = int(input())

shoes = year_tax - (40 / 100) * year_tax
outfit = shoes - (20 / 100) * shoes
ball = (1 / 4) * outfit
accessories = (1 / 5) * ball

total_price = year_tax + shoes + outfit + ball + accessories

print(total_price)