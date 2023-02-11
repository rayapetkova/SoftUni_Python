
total = 0

while True:
    line = input()
    if line == "special" or line == "regular":
        if total == 0:
            print(f"Invalid order!")
        else:
            taxes = (20 / 100) * total
            print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total:.2f}$\n"
                  f"Taxes: {taxes:.2f}$")
            print("-----------")
            if line == "regular":
                print(f"Total price: {(total + taxes):.2f}$")
            elif line == "special":
                print(f"Total price: {((total + taxes) - (10 / 100) * (total + taxes)):.2f}$")
        break
    price = float(line)
    if not price > 0:
        print(f"Invalid price!")
        continue
    total += price
