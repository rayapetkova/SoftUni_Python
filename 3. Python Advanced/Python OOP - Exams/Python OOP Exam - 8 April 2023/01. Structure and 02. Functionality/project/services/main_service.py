from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        final = [f"{self.name} Main Service:"]

        if self.robots:
            final.append(f"Robots: {' '.join(r.name for r in self.robots)}")
        else:
            final.append(f"Robots: none")

        return '\n'.join(final)
