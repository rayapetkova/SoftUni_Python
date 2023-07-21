from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        return f"Drink: {self.name}, {self.energy}"
