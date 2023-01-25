total = 0

while True:
    money = input()

    if money == "NoMoreMoney":
        break
    money = float(money)

    if money >= 0:
        print(f"Increase: {money:.2f}")
        total = total + money
    elif money < 0:
        print(f"Invalid operation!")
        break
print(f"Total: {total:.2f}")