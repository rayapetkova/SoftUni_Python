from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Service name cannot be empty!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(f"Service capacity cannot be less than or equal to 0!")

        self.__capacity = value

    @abstractmethod
    def details(self):
        pass
