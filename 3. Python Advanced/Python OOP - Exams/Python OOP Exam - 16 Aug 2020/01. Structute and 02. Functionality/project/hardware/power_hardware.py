from math import floor

from project.hardware.hardware import Hardware


# def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power",
                         floor(0.25 * capacity),
                         floor(memory + 0.75 * memory))
