
max_goals = 0
last_name = ""
hat_trick = False

while True:
    name = input()
    if name == "END":
        break
    if name != "END":
        goals = int(input())
        if goals > max_goals:
            max_goals = goals
            last_name = name
            if 3 <= max_goals < 10:
                hat_trick = True
            elif max_goals >= 10:
                hat_trick = True
                last_name = name
                break
            elif max_goals < 3:
                hat_trick = False

print(f"{last_name} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")