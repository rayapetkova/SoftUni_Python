n = int(input())
dictionary = {}

for i in range(n):
    text = input().split("|")
    curr_car, mileage, curr_fuel = text[0], int(text[1]), int(text[2])
    dictionary[curr_car] = {'mileage': mileage, 'fuel': curr_fuel}

while True:
    line = input()
    if line == "Stop":
        break
    command = line.split(" : ")
    if "Drive" in command:
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if dictionary[car]['fuel'] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            dictionary[car]['mileage'] += distance
            dictionary[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dictionary[car]['mileage'] >= 100000:
            del dictionary[car]
            print(f"Time to sell the {car}!")

    elif "Refuel" in command:
        car, kilometers = command[1], int(command[2])
        current_fuel = dictionary[car]['fuel']
        dictionary[car]['fuel'] = min(dictionary[car]['fuel'] + kilometers, 75)
        if dictionary[car]['fuel'] == 75:
            print(f"{car} refueled with {75 - current_fuel} liters")
        else:
            print(f"{car} refueled with {kilometers} liters")

    elif "Revert" in command:
        car, kilometers = command[1], int(command[2])
        dictionary[car]['mileage'] -= kilometers
        if dictionary[car]['mileage'] < 10000:
            dictionary[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in dictionary.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")