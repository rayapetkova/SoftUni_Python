n_km = int(input())
time_when_travel = input()
taxi = 0.70

if n_km < 20:
    if time_when_travel == "day":
        all_travel = n_km * 0.79 + taxi
        print(f"{all_travel:.2f}")
    elif time_when_travel == "night":
        all_travel = n_km * 0.90 + taxi
        print(f"{all_travel:.2f}")
elif 20 <= n_km < 100:
    all_travel = n_km * 0.09
    print(f"{all_travel:.2f}")
elif n_km >= 100:
    all_travel = n_km * 0.06
    print(f"{all_travel:.2f}")