from project.services.base_service import BaseService
from project.services.secondary_service import SecondaryService
from project.services.main_service import MainService
from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        dictionary = {"MainService": MainService, "SecondaryService": SecondaryService}

        if service_type not in dictionary.keys():
            raise Exception(f"Invalid service type!")

        curr_service = dictionary[service_type](name)
        self.services.append(curr_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        dictionary_valid_robots = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

        if robot_type not in dictionary_valid_robots:
            raise Exception(f"Invalid robot type!")

        curr_robot = dictionary_valid_robots[robot_type](name, kind, price)
        self.robots.append(curr_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in self.robots if r.name == robot_name][0]

        if (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService") or \
                (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService"):
            return f"Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception(f"Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]

        for curr_robot in service.robots:
            if curr_robot.name == robot_name:
                service.robots.remove(curr_robot)
                self.robots.append(curr_robot)
                return f"Successfully removed {robot_name} from {service_name}."

        raise Exception(f"No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        fed_robots = 0

        for curr_robot in service.robots:
            curr_robot.eating()
            fed_robots += 1

        return f"Robots fed: {fed_robots}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total = 0

        for curr_robot in service.robots:
            total += curr_robot.price

        return f"The value of service {service_name} is {total:.2f}."

    def __str__(self):
        final = []

        for curr_service in self.services:
            final.append(curr_service.details())

        return "\n".join(final)


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
