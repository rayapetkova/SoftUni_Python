from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception(f"User already exists!")

        curr_user = User(username, age)
        self.users_collection.append(curr_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        user = [u for u in self.users_collection if u.username == username]

        if not user:
            raise Exception(f"This user does not exist!")

        curr_user = user[0]
        if movie.owner.username != curr_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")

        curr_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs):
        dictionary = {
            'title': movie.title,
            'year': movie.year,
            'age_restriction': movie.age_restriction
        }

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        curr_user = [u for u in self.users_collection if u.username == username][0]
        if movie.owner.username != curr_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            dictionary[key] = value

        movie.title = dictionary['title']
        movie.year = dictionary['year']
        movie.age_restriction = dictionary['age_restriction']

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie):
        curr_user = [u for u in self.users_collection if u.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != curr_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        curr_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):
        curr_user = [u for u in self.users_collection if u.username == username][0]

        if movie.owner.username == curr_user.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in curr_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        curr_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        curr_user = [u for u in self.users_collection if u.username == username][0]

        if movie not in curr_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        curr_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."

        final = []

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        for movie in sorted_movies:
            final.append(movie.details())

        return '\n'.join(final)

    def __str__(self):
        final = []

        if not self.users_collection:
            final.append(f"All users: No users.")
        else:
            final.append(f"All users: {', '.join([u.username for u in self.users_collection])}")

        if not self.movies_collection:
            final.append(f"All movies: No movies.")
        else:
            final.append(f"All movies: {', '.join([m.title for m in self.movies_collection])}")

        return '\n'.join(final)


# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)
#
# for u in movie_app.users_collection:
#     print(u)
