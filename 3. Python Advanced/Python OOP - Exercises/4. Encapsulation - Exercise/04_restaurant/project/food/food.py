from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.__grams = grams


    @property
    def __grams(self):
        return self.grams

    @__grams.setter
    def __grams(self, value):
        self.grams = value
