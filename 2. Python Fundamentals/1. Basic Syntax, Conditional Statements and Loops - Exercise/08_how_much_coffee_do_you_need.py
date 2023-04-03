coffees_needed = 0

while True:
    string_given = input()
    if string_given == "END":
        if coffees_needed > 5:
            print(f"You need extra sleep")
        else:
            print(coffees_needed)
        break
    if string_given == "coding" or string_given == "dog" or string_given == "cat" or string_given == "movie":
        coffees_needed += 1
    elif string_given == "CODING" or string_given == "DOG" or string_given == "CAT" or string_given == "MOVIE":
        coffees_needed += 2
    else:
        continue
