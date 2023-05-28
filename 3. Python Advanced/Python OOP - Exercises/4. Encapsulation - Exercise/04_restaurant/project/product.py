class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def __name(self):
        return self.name

    @__name.setter
    def __name(self, value):
        self.name = value

    @property
    def __price(self):
        return self.price

    @__price.setter
    def __price(self, value):
        self.price = value
