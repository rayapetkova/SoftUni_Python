needed_experience = float(input())
count_of_battles = int(input())
total = 0
counter = 0
success = False

for i in range(1, count_of_battles + 1):
    experience = float(input())
    total += experience
    counter += 1
    if i % 3 == 0:
        total += (15 / 100) * experience
    if i % 5 == 0:
        total -= (10 / 100) * experience
    if i % 15 == 0:
        total += (5 / 100) * experience
    if total >= needed_experience:
        success = True
        print(f"Player successfully collected his needed experience for {counter} battles.")
        break

if not success:
    print(f"Player was not able to collect the needed experience, {(needed_experience - total):.2f} more needed.")