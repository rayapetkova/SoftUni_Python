from project.booths.booth import Booth


class PrivateBooth(Booth):
    def reserve(self, number_of_people: int):
        total = 3.50 * number_of_people
        self.price_for_reservation = total
        self.is_reserved = True
