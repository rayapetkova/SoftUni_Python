from math import floor

from project.hardware.hardware import Hardware


# def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy",
                         capacity * 2,
                         floor(0.75 * memory))
