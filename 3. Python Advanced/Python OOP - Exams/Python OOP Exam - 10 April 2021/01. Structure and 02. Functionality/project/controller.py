from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_TYPES_AQUARIUMS = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium
    }

    VALID_TYPES_DECORATIONS = {
        'Ornament': Ornament,
        'Plant': Plant
    }

    VALID_TYPES_FISH = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in Controller.VALID_TYPES_AQUARIUMS:
            return f"Invalid aquarium type."

        curr_aquarium = Controller.VALID_TYPES_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(curr_aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in Controller.VALID_TYPES_DECORATIONS:
            return f"Invalid decoration type."

        curr_decoration = Controller.VALID_TYPES_DECORATIONS[decoration_type]()
        self.decorations_repository.add(curr_decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type]

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        curr_decoration = decoration[0]

        curr_aquarium = None
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if not aquarium:
            return
        curr_aquarium = aquarium[0]

        curr_aquarium.decorations.append(curr_decoration)
        self.decorations_repository.decorations.remove(curr_decoration)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in Controller.VALID_TYPES_FISH:
            return f"There isn't a fish of type {fish_type}."

        curr_fish = Controller.VALID_TYPES_FISH[fish_type](fish_name, fish_species, price)

        curr_aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        return curr_aquarium.add_fish(curr_fish)

    def feed_fish(self, aquarium_name: str):
        curr_aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        curr_aquarium.feed()
        return f"Fish fed: {len(curr_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        curr_aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        fish_value = sum([f.price for f in curr_aquarium.fish])
        decorations_value = sum([d.price for d in curr_aquarium.decorations])

        return f"The value of Aquarium {aquarium_name} is {(fish_value + decorations_value):.2f}."

    def report(self):
        final_result = [str(a) for a in self.aquariums]

        return '\n'.join(final_result)
