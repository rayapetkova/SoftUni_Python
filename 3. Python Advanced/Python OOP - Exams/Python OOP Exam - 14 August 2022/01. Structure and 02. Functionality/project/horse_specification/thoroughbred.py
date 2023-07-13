from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140

    def train(self):
        new = self.speed + 3

        if new > Thoroughbred.max_speed:
            self.speed = 140
        else:
            self.speed += 3
