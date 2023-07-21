from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES_COMPUTERS = {
        'Desktop Computer': DesktopComputer,
        'Laptop': Laptop
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ComputerStoreApp.VALID_TYPES_COMPUTERS.keys():
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = ComputerStoreApp.VALID_TYPES_COMPUTERS[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        curr_computer = None

        for computer in self.warehouse:
            if computer.price <= client_budget and \
                    computer.processor == wanted_processor and \
                    computer.ram >= wanted_ram:
                curr_computer = computer

        if not curr_computer:
            raise Exception(f"Sorry, we don't have a computer for you.")

        self.warehouse.remove(curr_computer)

        profit = client_budget - curr_computer.price
        self.profits += profit

        return f"{curr_computer} sold for {client_budget}$."


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
