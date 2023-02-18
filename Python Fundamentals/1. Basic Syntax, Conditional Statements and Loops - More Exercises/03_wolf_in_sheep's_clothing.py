animals = input().split(", ")
an = list(animals)

if an[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    result = an.index("wolf")
    print(f"Oi! Sheep number {(len(an) - 1) - result}! You are about to be eaten by a wolf!")