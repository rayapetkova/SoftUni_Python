# isupper() - проверява дали символът е главна буква
# islower() - проверява дали символът е малка буква

max_movies = 7

best_movie = ''
best_movie_points = 0

for num_movie in range(1, max_movies + 1):
    movie = input()  # Matrix  # matrix

    if movie == "STOP":
        break
    movie_points = 0

    for symbol in movie:
        ascii_value = ord(symbol)
        movie_length = len(movie)

        if symbol.islower():
            ascii_value = ascii_value - 2 * movie_length
        elif symbol.isupper():
            ascii_value = ascii_value - movie_length

        movie_points = movie_points + ascii_value  # movie_points += ascii_value

    if movie_points > best_movie_points:
        best_movie = movie
        best_movie_points = movie_points

    if num_movie == 7:
        print(f"The limit is reached.")

print(f"The best movie for you is {best_movie} with {best_movie_points} ASCII sum.")