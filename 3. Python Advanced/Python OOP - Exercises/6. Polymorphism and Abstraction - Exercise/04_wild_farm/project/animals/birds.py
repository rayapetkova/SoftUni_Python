from project.animals.animal import Animal, Bird, Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    INCREASE_WEIGHT = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Owl.INCREASE_WEIGHT * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    INCREASE_WEIGHT = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return f"Cluck"

    def feed(self, food):
        self.weight += Hen.INCREASE_WEIGHT * food.quantity
        self.food_eaten += food.quantity
