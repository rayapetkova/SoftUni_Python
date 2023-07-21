from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }

    MAX_RAM = 128
    TYPE_COMPUTER = "desktop computer"

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
