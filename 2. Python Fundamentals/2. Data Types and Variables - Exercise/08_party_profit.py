people = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        people = people - 2
    if i % 15 == 0:
        people = people + 5

    coins = coins + (50 - 2 * people)

    if i % 3 == 0:
        coins = coins - 3 * people
    if i % 5 == 0:
        coins = coins + 20 * people
    if i % 3 == 0 and i % 5 == 0:
        coins = coins - 2 * people

coins_per_person = coins // people
print(f"{people} companions received {coins_per_person} coins each.")