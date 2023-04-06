max_goals = 0
best_player = ""
goals = 0
hat_trick = False

while True:
    name = input()
    if name == "END":
        break

    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = name
        if goals >= 3:
            hat_trick = True
        if goals >= 10:
            hat_trick = True
            break

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")