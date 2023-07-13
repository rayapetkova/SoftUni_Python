from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def work(self):
        pass


class RegularWorker(Worker):
    def work(self):
        print("I'm working!!")


class SuperWorker(Worker):
    def work(self):
        print("I work very hard!!!")


class BestWorker(Worker):
    def work(self):
        print("I'm not working at the moment because I'm the best!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, Worker):
            raise AssertionError(f"`worker` must be of type {Worker}")

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


regular_worker = RegularWorker()
manager = Manager()
manager.set_worker(regular_worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
