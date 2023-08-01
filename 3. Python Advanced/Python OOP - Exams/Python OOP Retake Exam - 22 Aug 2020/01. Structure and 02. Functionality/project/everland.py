class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0

        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        final = []

        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= (room.expenses + room.room_cost)
                final.append(f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                final.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(final)

    def status(self):
        final = [f"Total population: {sum([r.members_count for r in self.rooms])}"]

        for room in self.rooms:
            final.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")

            for n in range(1, len(room.children) + 1):
                final.append(f"--- Child {n} monthly cost: {room.children[n - 1].get_monthly_expense():.2f}$")

            final.append(f"--- Appliances monthly cost: {(sum([a.get_monthly_expense() for a in room.appliances])):.2f}$")

        return '\n'.join(final)
