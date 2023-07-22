from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.race import Race
from project.driver import Driver


class Controller:
    VALID_TYPES = {
        'MuscleCar': MuscleCar,
        'SportsCar': SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in Controller.VALID_TYPES:
            return

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        curr_car = Controller.VALID_TYPES[car_type](model, speed_limit)
        self.cars.append(curr_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        curr_driver = Driver(driver_name)
        self.drivers.append(curr_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        curr_race = Race(race_name)
        self.races.append(curr_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name]

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        curr_driver = driver[0]

        car = [c for c in self.cars[::-1] if c.__class__.__name__ == car_type]

        curr_car = None

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        for c in car:
            if not c.is_taken:
                curr_car = c
                break

        if not curr_car:
            raise Exception(f"Car {car_type} could not be found!")

        if curr_driver.car:
            old_model = curr_driver.car.model
            curr_driver.car.is_taken = False

            curr_driver.car = curr_car
            curr_car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_model} to {curr_car.model}."

        curr_driver.car = curr_car
        curr_car.is_taken = True

        return f"Driver {driver_name} chose the car {curr_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = [r for r in self.races if r.name == race_name]

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        curr_race = race[0]

        driver = [d for d in self.drivers if d.name == driver_name]

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        curr_driver = driver[0]

        if not curr_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if curr_driver in curr_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        curr_race.drivers.append(curr_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        curr_race = race[0]

        if len(curr_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_cars = sorted(curr_race.drivers, key=lambda x: -x.car.speed_limit)
        three_fastest_cars = sorted_cars[0:3]

        final = []
        for fast_driver in three_fastest_cars:
            fast_driver.number_of_wins += 1

            final.append(f"Driver {fast_driver.name} wins the {race_name} race with a speed of {fast_driver.car.speed_limit}.")

        return '\n'.join(final)


# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# print(controller.add_car_to_driver("Jack", "MuscleCar"))
# print(controller.add_car_to_driver("John", "SportsCar"))
# print(controller.create_race("Christmas Top Racers"))
# print(controller.add_driver_to_race("Christmas Top Racers", "John"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
# print(controller.start_race("Christmas Top Racers"))
# [print(d.name, d.number_of_wins) for d in controller.drivers]
