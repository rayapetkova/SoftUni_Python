from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        ...

    def __repr__(self):
        return f"This is {self.name}. Sound that {self.name} is making: {self.make_sound()}"


class Dog(Animal):
    def make_sound(self):
        return f"woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Cow(Animal):
    def make_sound(self):
        return f"Muuuuu"


animals = [Dog("Duke"), Cat("Lady"), Cow("Bailey")]
for animal in animals:
    print(animal.make_sound())
    print(animal)
    print()
