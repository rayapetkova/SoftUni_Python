rest_days = int(input())
left_time = 0

work_days = 365 - rest_days
play_time = work_days * 63 + rest_days * 127
hours = play_time // 60
minutes = play_time % 60

if play_time > 30000:
    left_time = play_time - 30000
    hours = left_time // 60
    minutes = left_time % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
elif play_time < 30000:
    left_time = 30000 - play_time
    hours = left_time // 60
    minutes = left_time % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")