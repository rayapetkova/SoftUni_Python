goal_steps = 10000

walked_steps = 0

while True:
    steps = input()
    if steps != "Going home":
        steps = int(steps)
        walked_steps = walked_steps + steps
        if walked_steps >= 10000:
            print(f"Goal reached! Good job!")
            print(f"{walked_steps - 10000} steps over the goal!")
            break

    if steps == "Going home":
        steps_to_home = int(input())
        walked_steps = walked_steps + steps_to_home
        if walked_steps >= 10000:
            print(f"Goal reached! Good job!")
            print(f"{walked_steps - 10000} steps over the goal!")
        else:
            print(f"{10000 - walked_steps} more steps to reach goal.")
        break