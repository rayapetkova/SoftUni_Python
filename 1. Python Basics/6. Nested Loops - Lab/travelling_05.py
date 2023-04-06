

while True:
    destination = input()

    if destination == "End":
        break

    budget = float(input())
    all_sum = 0

    while True:
        sum1 = float(input())
        all_sum = all_sum + sum1
        if all_sum >= budget:
            print(f"Going to {destination}!")
            break