time_for_photos = int(input())
number_scenes = int(input())
time_per_scene = int(input())

field_preparation = 0.15 * time_for_photos
scenes_total_time = number_scenes * time_per_scene

total_time_needed = field_preparation + scenes_total_time

if time_for_photos >= total_time_needed:
    time_left = time_for_photos - total_time_needed
    print(f"You managed to finish the movie on time! You have {round(time_left)} minutes left!")
else:
    time_needed = total_time_needed - time_for_photos
    print(f"Time is up! To complete the movie you need {round(time_needed)} minutes.")
