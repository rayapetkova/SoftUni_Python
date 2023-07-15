class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError(f"Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError(f"Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        final = [f"Username: {self.username}, Age: {self.age}\nLiked movies:"]

        if self.movies_liked:
            final.append('\n'.join([m.details() for m in self.movies_liked]))
        else:
            final.append(f"No movies liked.")

        final.append(f"Owned movies:")

        if self.movies_owned:
            final.append('\n'.join([m.details() for m in self.movies_owned]))
        else:
            final.append(f"No movies owned.")

        return '\n'.join(final)
