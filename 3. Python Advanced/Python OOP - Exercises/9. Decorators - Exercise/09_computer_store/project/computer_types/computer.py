from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    AVAILABLE_PROCESSORS = {}
    MAX_RAM = 0
    TYPE_COMPUTER = ""

    @abstractmethod
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError(f"Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError(f"Model name cannot be empty.")

        self.__model = value

    def get_power(self, needed_ram: int):
        result = log2(needed_ram)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with {self.TYPE_COMPUTER} {self.manufacturer} {self.model}!")

        if not self.get_power(ram) or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.TYPE_COMPUTER} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_PROCESSORS[processor]
        self.price += int(log2(ram)) * 100

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
