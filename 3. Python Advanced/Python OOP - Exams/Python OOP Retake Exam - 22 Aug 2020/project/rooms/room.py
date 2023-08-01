from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError(f"Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total = 0

        for lst in args:
            for a in lst:
                total += a.get_monthly_expense()

        self.expenses = total
