from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:
    types_delicacies = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
        }

    types_booths = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in self.types_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        curr_delicacy = ChristmasPastryShopApp.types_delicacies[type_delicacy](name, price)
        self.delicacies.append(curr_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.types_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        curr_booth = ChristmasPastryShopApp.types_booths[type_booth](booth_number, capacity)
        self.booths.append(curr_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = [b for b in self.booths if b.booth_number == booth_number]

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        curr_booth = booth[0]

        delicacy = [d for d in self.delicacies if d.name == delicacy_name]

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        curr_delicacy = delicacy[0]

        curr_booth.delicacy_orders.append(curr_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        curr_booth = [b for b in self.booths if b.booth_number == booth_number][0]

        orders_price = sum([o.price for o in curr_booth.delicacy_orders])
        total = curr_booth.price_for_reservation + orders_price
        self.income += total
        curr_booth.delicacy_orders = []
        curr_booth.is_reserved = False
        curr_booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {total:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


# Test code:

# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
