from Python_OOP.exam_prep.april_exam_2023.project.robots.female_robot import FemaleRobot
from Python_OOP.exam_prep.april_exam_2023.project.robots.male_robot import MaleRobot
from Python_OOP.exam_prep.april_exam_2023.project.services.main_service import MainService
from Python_OOP.exam_prep.april_exam_2023.project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VIABLE_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    VIABLE_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type not in self.VIABLE_SERVICES:
            raise Exception("Invalid service type!")
        service = self.VIABLE_SERVICES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.VIABLE_ROBOTS:
            raise Exception("Invalid robot type!")
        robot = self.VIABLE_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if isinstance(robot, MaleRobot) and isinstance(service, MainService):
            if service.capacity > len(service.robots):
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")

        elif isinstance(robot, FemaleRobot) and isinstance(service, SecondaryService):
            if service.capacity > len(service.robots):
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        r = robot[0]
        service.robots.remove(r)
        self.robots.append(r)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        price = 0
        for robot in service.robots:
            price += robot.price

        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        result = ""

        for service in self.services:
            result += f"{service.details()}\n"

        return result[:-1]