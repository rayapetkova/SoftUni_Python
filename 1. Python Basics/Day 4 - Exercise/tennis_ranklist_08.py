import math

tournament_count = int(input())
start_points = int(input())

points = start_points
wins = 0
finals = 0
semi_finals = 0

for i in range(1, tournament_count + 1):
    stage = input()
    if stage == "W":
        wins = wins + 1
        points = points + 2000
    elif stage == "F":
        finals = finals + 1
        points = points + 1200
    elif stage == "SF":
        semi_finals = semi_finals + 1
        points = points + 720

print(f"Final points: {points}")

average_points = (points - start_points) / tournament_count
print(f"Average points: {math.floor(average_points)}")

percents_wins = (wins / tournament_count) * 100
print(f"{percents_wins:.2f}%")