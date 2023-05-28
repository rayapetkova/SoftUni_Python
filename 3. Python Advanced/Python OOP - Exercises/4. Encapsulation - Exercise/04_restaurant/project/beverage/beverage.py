from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def __milliliters(self):
        return self.milliliters

    @__milliliters.setter
    def __milliliters(self, value):
        self.milliliters = value
