from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 50)

    def add_fish(self, fish):
        if not self.capacity:
            return f"Not enough capacity."

        if fish.__class__.__name__ == "FreshwaterFish":
            self.fish.append(fish)
            self.capacity -= 1
            return f"Successfully added FreshwaterFish to {self.name}."
        else:
            return f"Water not suitable."