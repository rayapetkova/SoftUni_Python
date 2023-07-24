from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class SpaceStation:
    VALID_TYPES = {
        'Biologist': Biologist,
        'Geodesist': Geodesist,
        'Meteorologist': Meteorologist
    }

    SUCCESSFUL = 0
    UNSUCCESSFUL = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                return f"{name} is already added."

        if astronaut_type not in SpaceStation.VALID_TYPES:
            raise Exception(f"Astronaut type is not valid!")

        curr_astronaut = SpaceStation.VALID_TYPES[astronaut_type](name)
        self.astronaut_repository.add(curr_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for p in self.planet_repository.planets:
            if p.name == name:
                return f"{name} is already added."

        curr_planet = Planet(name)
        split_items = items.split(", ")

        for i in split_items:
            curr_planet.items.append(i)

        self.planet_repository.add(curr_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        curr_astronaut = astronaut[0]
        self.astronaut_repository.remove(curr_astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = [p for p in self.planet_repository.planets if p.name == planet_name]

        if not planet:
            raise Exception(f"Invalid planet name!")
        curr_planet = planet[0]

        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)

        total = []
        for a in sorted_astronauts:
            if a.oxygen > 30:
                total.append(a)

        if not total:
            raise Exception(f"You need at least one astronaut to explore the planet!")

        participated = 0
        for astronaut in total[0:5]:
            while astronaut.oxygen:
                if curr_planet.items:
                    item = curr_planet.items.pop()
                    astronaut.backpack.append(item)
                    astronaut.breathe()

                else:
                    participated += 1
                    SpaceStation.SUCCESSFUL += 1
                    return f"Planet: {planet_name} was explored. {participated} astronauts participated in collecting items."

            participated += 1

        SpaceStation.UNSUCCESSFUL += 1
        return f"Mission is not completed."

    def report(self):
        final = [f"{SpaceStation.SUCCESSFUL} successful missions!\n"
                 f"{SpaceStation.UNSUCCESSFUL} missions were not completed!\n"
                 f"Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            final.append(f"Name: {a.name}\nOxygen: {a.oxygen}")

            if a.backpack:
                final.append(f"Backpack items: {', '.join([item for item in a.backpack])}")
            else:
                final.append(f"Backpack items: none")

        return '\n'.join(final)
