countries = input().split(", ")
capitals = input().split(", ")

final = dict(zip(countries, capitals))

[print(f"{country} -> {capital}") for country, capital in final.items()]