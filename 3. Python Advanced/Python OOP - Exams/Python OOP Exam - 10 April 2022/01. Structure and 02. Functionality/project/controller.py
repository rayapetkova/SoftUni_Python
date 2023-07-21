from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                added.append(player)

        return f"Successfully added: {', '.join([p.name for p in added])}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        curr_supply, curr_player = None, None

        for supply in self.supplies[::-1]:
            if supply.__class__.__name__ == sustenance_type:
                curr_supply = supply
                break

        player = [p for p in self.players if p.name == player_name]
        if player:
            curr_player = player[0]
        else:
            return

        if curr_player.stamina == 100:
            return f"{player_name} have enough stamina."

        if not curr_supply:
            if sustenance_type == "Food":
                raise Exception(f"There are no food supplies left!")
            elif sustenance_type == "Drink":
                raise Exception(f"There are no drink supplies left!")

            return

        if curr_supply.energy + curr_player.stamina > 100:
            curr_player.stamina = 100
        else:
            curr_player.stamina += curr_supply.energy

        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i] == curr_supply:
                self.supplies.pop(i)
                break

        return f"{player_name} sustained successfully with {curr_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first = [p1 for p1 in self.players if p1.name == first_player_name][0]
        second = [p2 for p2 in self.players if p2.name == second_player_name][0]

        result = []
        if first.stamina == 0:
            result.append(f"Player {first_player_name} does not have enough stamina.")
        if second.stamina == 0:
            result.append(f"Player {second_player_name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

        def curr_duel(smaller, greater):
            result = greater.stamina - smaller.stamina / 2

            if result <= 0:
                greater.stamina = 0
                return f"Winner: {smaller.name}"
            else:
                greater.stamina = result

            result2 = smaller.stamina - greater.stamina / 2
            if result2 <= 0:
                smaller.stamina = 0
                return f"Winner: {greater.name}"
            else:
                smaller.stamina = result2

            if first.stamina > second.stamina:
                return f"Winner: {first.name}"

            return f"Winner: {second.name}"

        if first.stamina < second.stamina:
            return curr_duel(first, second)

        elif first.stamina > second.stamina:
            return curr_duel(second, first)

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        final = []

        for player in self.players:
            final.append(str(player))

        for supply in self.supplies:
            final.append(supply.details())

        return '\n'.join(final)


# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
