num = int(input())

counter = 0
fourth_number = ""
found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == num and a < b and c > d and 4 <= num <= 144:
                    counter = counter + 1
                    if counter >= 4:
                        found = True
                        print(f"{a}{b}{c}{d}", end=" ")
                        if counter == 4:
                            fourth_number = str(a) + str(b) + str(c) + str(d)
                    else:
                        print(f"{a}{b}{c}{d}", end=" ")
if found == False:
    print()
    print("No!")

print()
if found:
    print(f"Password: {fourth_number}")