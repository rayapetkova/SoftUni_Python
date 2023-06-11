from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        self.gender = "Male"
        super().__init__(name, age, self.gender)

    def make_sound(self):
        return f"Hiss"
