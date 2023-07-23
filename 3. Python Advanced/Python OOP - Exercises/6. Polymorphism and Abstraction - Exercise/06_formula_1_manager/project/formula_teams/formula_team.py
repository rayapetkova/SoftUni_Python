from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses_per_race(self):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        total = 0

        for sponsor in self.sponsors.values():
            for pos in sponsor:
                if race_pos <= pos:
                    total += sponsor[pos]
                    break

        total -= self.expenses_per_race
        self.budget += total

        return f"The revenue after the race is {total}$. Current budget {self.budget}$"
