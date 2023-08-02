from math import floor

from project.software.software import Software


# def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name,
                         "Light",
                         floor(capacity_consumption + 0.5 * capacity_consumption),
                         floor(memory_consumption - 0.5 * memory_consumption))
