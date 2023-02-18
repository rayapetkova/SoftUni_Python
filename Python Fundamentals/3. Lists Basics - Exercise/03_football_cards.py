team_A = ["A-" + str(chr1) for chr1 in range(1, 12)]
team_B = ["B-" + str(chr2) for chr2 in range(1, 12)]
players = input().split()
terminated_game = False

for i in players:
    if i in team_A:
        team_A.remove(i)
    elif i in team_B:
        team_B.remove(i)
    if len(team_A) < 7 or len(team_B) < 7:
        terminated_game = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminated_game:
    print("Game was terminated")