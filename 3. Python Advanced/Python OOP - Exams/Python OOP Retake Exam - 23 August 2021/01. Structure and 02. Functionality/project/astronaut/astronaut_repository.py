class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = [a for a in self.astronauts if a.name == name]

        if astronaut:
            return astronaut[0]
