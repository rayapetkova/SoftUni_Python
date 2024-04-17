max_movies = 7
best_movie = ''
best_points = 0

for num_movie in range(1, max_movies + 1):
    movie = input()  # Matrix

    if movie == "STOP":
        break
    current_points = 0

    for symbol in movie:  # M
        ascii_value = ord(symbol)  # 77

        if symbol.isupper():
            ascii_value -= len(movie)
        elif symbol.islower():
            ascii_value -= 2 * len(movie)

        current_points += ascii_value

    if current_points >= best_points:
        best_points = current_points
        best_movie = movie

    if num_movie == 7:
        print(f"The limit is reached.")

print(f"The best movie for you is {best_movie} with {best_points} ASCII sum.")