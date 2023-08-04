from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        'MainService': MainService,
        'SecondaryService': SecondaryService
    }

    VALID_ROBOTS = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.VALID_SERVICES.keys():
            raise Exception(f"Invalid service type!")

        curr_service = RobotsManagingApp.VALID_SERVICES[service_type](name)
        self.services.append(curr_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in RobotsManagingApp.VALID_ROBOTS.keys():
            raise Exception(f"Invalid robot type!")

        curr_robot = RobotsManagingApp.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(curr_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        curr_robot = [r for r in self.robots if r.name == robot_name][0]
        curr_service = [s for s in self.services if s.name == service_name][0]

        if (curr_robot.__class__.__name__ == "FemaleRobot" and curr_service.__class__.__name__ == "MainService") or \
            (curr_robot.__class__.__name__ == "MaleRobot" and curr_service.__class__.__name__ == "SecondaryService"):
            return f"Unsuitable service."

        if len(curr_service.robots) == curr_service.capacity:
            raise Exception(f"Not enough capacity for this robot!")

        self.robots.remove(curr_robot)
        curr_service.robots.append(curr_robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        curr_service = [s for s in self.services if s.name == service_name][0]

        robot = [r for r in curr_service.robots if r.name == robot_name]
        if not robot:
            raise Exception(f"No such robot in this service!")
        curr_robot = robot[0]

        curr_service.robots.remove(curr_robot)
        self.robots.append(curr_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        curr_service = [s for s in self.services if s.name == service_name][0]

        for robot in curr_service.robots:
            robot.eating()

        return f"Robots fed: {len(curr_service.robots)}."

    def service_price(self, service_name: str):
        curr_service = [s for s in self.services if s.name == service_name][0]
        total_price = sum([r.price for r in curr_service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        final = []

        for service in self.services:
            final.append(service.details())

        return '\n'.join(final)


# main_app = RobotsManagingApp()
# print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
# print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
# print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
# print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
#
# print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))
#
# print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
# print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
#
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))
#
# print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))
