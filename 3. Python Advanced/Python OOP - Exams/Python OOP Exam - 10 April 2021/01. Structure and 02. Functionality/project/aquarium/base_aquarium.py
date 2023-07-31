from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError(f"Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for one_fish in self.fish:
            one_fish.eat()

    def __str__(self):
        final = [f"{self.name}:"]

        if self.fish:
            final.append(f"Fish: {' '.join([f.name for f in self.fish])}")
        else:
            final.append(f"Fish: none")

        final.append(f"Decorations: {len(self.decorations)}")
        final.append(f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(final)
