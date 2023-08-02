from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        curr_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(curr_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        curr_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(curr_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]

        if not hardware:
            return f"Hardware does not exist"
        curr_hardware = hardware[0]

        curr_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        curr_hardware.install(curr_software)
        System._software.append(curr_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]

        if not hardware:
            return f"Hardware does not exist"
        curr_hardware = hardware[0]

        curr_software = LightSoftware(name, capacity_consumption, memory_consumption)
        curr_hardware.install(curr_software)
        System._software.append(curr_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]

        if not (hardware and software):
            return f"Some of the components do not exist"

        curr_hardware, curr_software = hardware[0], software[0]

        curr_hardware.uninstall(curr_software)
        System._software.remove(curr_software)

    @staticmethod
    def analyze():
        final = [f"System Analysis",
                 f"Hardware Components: {len(System._hardware)}",
                 f"Software Components: {len(System._software)}",
                 f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / "
                 f"{sum([h.memory for h in System._hardware])}",
                 f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / "
                 f"{sum([h.capacity for h in System._hardware])}"]

        return '\n'.join(final)

    @staticmethod
    def system_split():
        final = []

        for hardware in System._hardware:
            final.append(f"Hardware Component - {hardware.name}")
            final.append(f"Express Software Components: {len([e for e in hardware.software_components if e.software_type == 'Express'])}")
            final.append(f"Light Software Components: {len([e for e in hardware.software_components if e.software_type == 'Light'])}")
            final.append(f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])} / {hardware.memory}")
            final.append(f"Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])} / {hardware.capacity}")
            final.append(f"Type: {hardware.hardware_type}")

            if hardware.software_components:
                final.append(f"Software Components: {', '.join(s.name for s in hardware.software_components)}")
            else:
                final.append(f"None")

        return '\n'.join(final)

