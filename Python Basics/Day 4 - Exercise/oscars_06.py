actor_name = input()
start_points = float(input())
jury = int(input())

all_points = start_points

for i in range(1, jury + 1):
    jury_name = input()
    points_given = float(input())
    all_points = (len(jury_name) * points_given) / 2 + all_points
    if all_points >= 1250.5:
        break

if all_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - all_points):.1f} more!")