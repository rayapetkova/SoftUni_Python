from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        self.gender = "Female"
        super().__init__(name, age, self.gender)

    def make_sound(self):
        return f"Meow"
