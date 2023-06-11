from project.animals.animal import Animal, Bird, Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    INCREASE_WEIGHT = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Mouse.INCREASE_WEIGHT * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    INCREASE_WEIGHT = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Dog.INCREASE_WEIGHT * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    INCREASE_WEIGHT = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Cat.INCREASE_WEIGHT * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    INCREASE_WEIGHT = 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Tiger.INCREASE_WEIGHT * food.quantity
        self.food_eaten += food.quantity
