from math import floor

series_name = input()
number_seasons = int(input())
number_episodes = int(input())
time_per_episode = float(input())

ads_per_episode = 0.2 * time_per_episode
time_per_episode_with_ads = time_per_episode + ads_per_episode

special_minutes = number_seasons * 10

total_time = number_seasons * number_episodes * time_per_episode_with_ads + special_minutes

print(f"Total time needed to watch the {series_name} series is {floor(total_time)} minutes.")