from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__animal_capacity and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for some_worker in self.workers:
            if some_worker.name == worker_name:
                self.workers.remove(some_worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = 0

        for some_worker in self.workers:
            total += some_worker.salary

        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total = 0

        for some_animal in self.animals:
            total += some_animal.money_for_care

        if self.__budget >= total:
            self.__budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        c_animals = {'Lion': [], 'Tiger': [], 'Cheetah': []}

        for some_animal in self.animals:
            c_animals[some_animal.__class__.__name__].append(str(some_animal))

        final = [f"You have {len(self.animals)} animals",
                 f"----- {len(c_animals['Lion'])} Lions:", *c_animals['Lion'],
                 f"----- {len(c_animals['Tiger'])} Tigers:", *c_animals['Tiger'],
                 f"----- {len(c_animals['Cheetah'])} Cheetahs:", *c_animals['Cheetah']]

        return '\n'.join(final)

    def workers_status(self):
        c_workers = {'Keeper': [], 'Caretaker': [], 'Vet': []}

        for some_worker in self.workers:
            c_workers[some_worker.__class__.__name__].append(str(some_worker))

        final = [f"You have {len(self.workers)} workers",
                 f"----- {len(c_workers['Keeper'])} Keepers:", *c_workers['Keeper'],
                 f"----- {len(c_workers['Caretaker'])} Caretakers:", *c_workers['Caretaker'],
                 f"----- {len(c_workers['Vet'])} Vets:", *c_workers['Vet']]

        return '\n'.join(final)
