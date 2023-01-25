bottles = int(input())

all_ml = bottles * 750
counter = 0
pots = 0
plates = 0
over = False

while True:
    num_things = input()
    if num_things == "End":
        break
    if num_things != "End":
        if all_ml >= 0:
            num_things = int(num_things)
            counter = counter + 1
            if counter % 3 == 0:
                pots = pots + num_things
                all_ml = all_ml - num_things * 15
            else:
                plates = plates + num_things
                all_ml = all_ml - num_things * 5

        if all_ml < 0:
            over = True
            break

if over:
    print(f"Not enough detergent, {abs(all_ml)} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {all_ml} ml.")