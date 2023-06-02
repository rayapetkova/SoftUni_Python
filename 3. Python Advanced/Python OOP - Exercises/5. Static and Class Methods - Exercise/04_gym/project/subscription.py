class Subscription:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.id

    @staticmethod
    def get_next_id():
        current = Subscription.id
        Subscription.id += 1
        return current

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
