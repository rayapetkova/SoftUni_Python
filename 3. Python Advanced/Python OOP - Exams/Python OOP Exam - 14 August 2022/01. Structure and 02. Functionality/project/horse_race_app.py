import sys

from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    horse_types = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in HorseRaceApp.horse_types:
            curr_horse = HorseRaceApp.horse_types[horse_type](horse_name, horse_speed)
            self.horses.append(curr_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        curr_jockey = Jockey(jockey_name, age)
        self.jockeys.append(curr_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        curr_race = HorseRace(race_type)
        self.horse_races.append(curr_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        curr_jockey, curr_horse = None, None

        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                curr_horse = horse
                break

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                curr_jockey = jockey
                break

        if not curr_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not curr_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if curr_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        curr_horse.is_taken = True
        curr_jockey.horse = curr_horse
        return f"Jockey {jockey_name} will ride the horse {curr_jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        curr_jockey, curr_race = None, None

        for race in self.horse_races:
            if race.race_type == race_type:
                curr_race = race
                break

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                curr_jockey = jockey
                break

        if not curr_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not curr_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if curr_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if curr_jockey in curr_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        curr_race.jockeys.append(curr_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = [r for r in self.horse_races if r.race_type == race_type]

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        curr_race = race[0]

        if len(curr_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = max([j.horse.speed for j in curr_race.jockeys])

        c_jockey = [j for j in curr_race.jockeys if j.horse.speed == highest_speed][0]
        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {c_jockey.name}! Winner's horse: {c_jockey.horse.name}."


# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))
