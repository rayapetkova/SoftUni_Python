type_fuel = input()
L_in_tank = float(input())

if type_fuel == "Diesel":
    if L_in_tank >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")
elif type_fuel == "Gasoline":
    if L_in_tank >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")
elif type_fuel == "Gas":
    if L_in_tank >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")
else:
    print("Invalid fuel!")