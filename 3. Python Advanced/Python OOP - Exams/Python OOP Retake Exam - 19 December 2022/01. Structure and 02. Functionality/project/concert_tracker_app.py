from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    musician_types = {"Guitarist": Guitarist,
                      "Drummer": Drummer,
                      "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.musician_types.keys():
            raise ValueError(f"Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        curr_musician = ConcertTrackerApp.musician_types[musician_type](name, age)
        self.musicians.append(curr_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        curr_band = Band(name)
        self.bands.append(curr_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        curr_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(curr_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        dictionary_count = {"Guitarist": 0,
                            "Drummer": 0,
                            "Singer": 0}

        required_skills = {
            "Rock": ["play the drums with drumsticks", "sing high pitch notes", "play rock"],
            "Metal": ["play the drums with drumsticks", "sing low pitch notes", "play metal"],
            "Jazz": ["play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes", "play jazz"]
        }

        for member in band.members:
            if member.__class__.__name__ in ConcertTrackerApp.musician_types.keys():
                dictionary_count[member.__class__.__name__] += 1

        if not (dictionary_count["Guitarist"] and dictionary_count["Drummer"] and dictionary_count["Singer"]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        curr_skills = []
        for member in band.members:
            for skill in member.skills:
                curr_skills.append(skill)

        concert_happening = False

        for c_genre, skills in required_skills.items():
            counter = 0

            for s in skills:
                if s in curr_skills:
                    counter += 1

            if (counter == 3 and (c_genre == "Rock" or c_genre == "Metal")) or (counter == 4 and c_genre == "Jazz"):
                concert_happening = True
                break

        if not concert_happening:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        curr_concert = [c for c in self.concerts if c.place == concert_place][0]
        profit = (curr_concert.audience * curr_concert.ticket_price) - curr_concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {curr_concert.genre} concert in {concert_place}."


# musician_types = ["Singer", "Drummer", "Guitarist"]
# names = ["George", "Alex", "Lilly"]
#
# app = ConcertTrackerApp()
#
# for i in range(3):
#     print(app.create_musician(musician_types[i], names[i], 20))
#
# print(app.musicians[0].learn_new_skill("sing high pitch notes"))
# print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
# print(app.musicians[2].learn_new_skill("play rock"))
#
# print(app.create_band("RockName"))
# for i in range(3):
#     print(app.add_musician_to_band(names[i], "RockName"))
#
# print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.start_concert("Sofia", "RockName"))
