class Flower:
    def __init__(self, name: str, water_requirements: float):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        return f"{self.name} is happy" if self.is_happy else f"{self.name} is not happy"

# Test code:

# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(60)
# print(flower.status())
# flower.water(100)
# print(flower.status())
