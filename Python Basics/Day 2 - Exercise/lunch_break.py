from math import ceil

series_name = input()
one_episode_time = int(input())
break_time = int(input())

lunch = (1 / 8) * break_time
rest = (1 / 4) * break_time
break_time_without_lunch_and_rest = break_time - (lunch + rest)

if one_episode_time > break_time_without_lunch_and_rest:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(one_episode_time - break_time_without_lunch_and_rest)} more minutes.")
elif one_episode_time <= break_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(break_time_without_lunch_and_rest - one_episode_time)} minutes free time.")
