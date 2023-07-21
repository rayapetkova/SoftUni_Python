from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }

    MAX_RAM = 64
    TYPE_COMPUTER = "laptop"

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
