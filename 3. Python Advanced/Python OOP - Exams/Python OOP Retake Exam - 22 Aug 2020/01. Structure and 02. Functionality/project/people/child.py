class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(t for t in toys_cost)

    def get_monthly_expense(self):
        return self.cost * 30
