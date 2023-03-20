dictionary = {}

while True:
    line = input()
    if line == "stocked":
        break
    command = line.split()
    name, price, quantity = command[0], float(command[1]), int(command[2])
    dictionary[name] = dictionary.get(name, {'price': None, 'quantity': 0})
    dictionary[name]['price'] = price
    dictionary[name]['quantity'] += quantity

grand_total = 0
for key, value in dictionary.items():
    print(f"{key}: ${value['price']:.2f} * {value['quantity']} = ${value['price'] * value['quantity']:.2f}")
    grand_total += value['price'] * value['quantity']
print(f"------------------------------")
print(f"Grand Total: ${grand_total:.2f}")