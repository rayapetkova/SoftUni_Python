from project.dough import Dough
from project.topping import Topping

class Pizza:
    def __init__(self, name: str, dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")

        self.__name = value


    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value


    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        self.__max_number_of_toppings = value


    def add_topping(self, topping):
        if self.max_number_of_toppings <= len(self.toppings):
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight

        elif self.max_number_of_toppings > len(self.toppings):
            self.toppings[topping.topping_type] = topping.weight



    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
