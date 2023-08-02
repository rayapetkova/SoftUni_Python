from project.software.software import Software


# def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
class ExpressSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Express", capacity_consumption, memory_consumption * 2)
