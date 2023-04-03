made_snowballs = int(input())
the_best = 0
best_weight = 0
best_time = 0
best_quality = 0
best_snowball = 0
found = False

for i in range(1, made_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball = (weight / time) ** quality

    if snowball > the_best:
        the_best = snowball
        best_weight = weight
        best_time = time
        best_quality = quality
        best_snowball = (best_weight / best_time) ** best_quality
        found = True

if found:
    print(f"{best_weight} : {best_time} = {best_snowball:.0f} ({best_quality})")