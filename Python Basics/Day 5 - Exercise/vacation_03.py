trip_money = float(input())
start_money = float(input())

spend_counter = 0
days_counter = 0

while True:
    action = input()
    sum_money = float(input())

    if action == "spend":
        start_money = start_money - sum_money
        spend_counter = spend_counter + 1
        days_counter = days_counter + 1
        if sum_money > start_money:
            start_money = 0
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(f"{days_counter}")
            break

    if action == "save":
        start_money = start_money + sum_money
        spend_counter = 0
        days_counter = days_counter + 1
        if start_money >= trip_money:
            print(f"You saved the money for {days_counter} days.")
            break