from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    max_speed = 120

    def train(self):
        new = self.speed + 2

        if new > Appaloosa.max_speed:
            self.speed = 120
        else:
            self.speed += 2
