from abc import ABC, abstractmethod
import time


class Workable(ABC):
    def work(self):
        pass


class Eatable(ABC):
    def eat(self):
        pass


class RegularWorker(Workable, Eatable):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):
    def set_worker(self, worker):
        if not isinstance(worker, Workable):
            raise AssertionError(f"`worker` must be of type {Workable}")

        self.worker = worker

    def manage(self):
        self.worker.work()


class LunchBreakManager(BaseManager):
    def set_worker(self, worker):
        if not isinstance(worker, Eatable):
            raise AssertionError(f"`worker` must be of type {Eatable}")

    def lunch_break(self):
        self.worker.eat()


regular_worker = RegularWorker()
work_manager = WorkManager()
work_manager.set_worker(regular_worker)
work_manager.manage()

super_worker = SuperWorker()
work_manager.set_worker(super_worker)
work_manager.manage()

# This will raise an AssertionError because "robot" is not an instance of "Eatable"
lunch_break_manager = LunchBreakManager()
robot = Robot()
lunch_break_manager.set_worker(robot)
lunch_break_manager.lunch_break()
