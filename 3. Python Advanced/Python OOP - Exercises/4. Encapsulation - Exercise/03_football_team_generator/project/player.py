class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def __name(self):
        return self.name

    @__name.setter
    def __name(self, value):
        self.name = value

    def __str__(self):
        return f"Player: {self.__name}\nSprint: {self.__sprint}\n" \
               f"Dribble: {self.__dribble}\nPassing: {self.__passing}\n" \
               f"Shooting: {self.__shooting}"