from project.booths.booth import Booth


class OpenBooth(Booth):
    def reserve(self, number_of_people: int):
        total = 2.50 * number_of_people
        self.price_for_reservation = total
        self.is_reserved = True
