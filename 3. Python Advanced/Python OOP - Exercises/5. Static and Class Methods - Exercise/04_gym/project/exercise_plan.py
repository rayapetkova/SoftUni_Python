class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        minutes = hours * 60

        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        current = ExercisePlan.id
        ExercisePlan.id += 1
        return current

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
