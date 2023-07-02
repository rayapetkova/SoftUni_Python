class TennisPlayer:
    def __init__(self, name: str, age: int, points: float):
        self.name = name
        self.age = age
        self.points = points
        self.wins = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 2:
            raise ValueError("Name should be more than 2 symbols!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Players must be at least 18 years of age!")
        self.__age = value

    def add_new_win(self, tournament_name: str):
        if tournament_name not in self.wins:
            self.wins.append(tournament_name)
        else:
            return f"{tournament_name} has been already added to the list of wins!"

    def __lt__(self, other):
        if self.points < other.points:
            return f'{other.name} is a top seeded player and he/she is better than {self.name}'
        return f'{self.name} is a better player than {other.name}'

    def __str__(self):
        return f"Tennis Player: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Points: {self.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.wins)}"