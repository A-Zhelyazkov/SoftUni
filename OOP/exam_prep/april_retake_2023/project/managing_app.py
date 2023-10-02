from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_CARS = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
                }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name, last_name, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):
        if vehicle_type not in self.VALID_CARS:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_CARS[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):
        route_id = len(self.routes) + 1

        for route in self.routes:

            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            #TODO not sure
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count):
        damaged_cars = [v for v in self.vehicles if v.is_damaged]
        ordered = sorted(damaged_cars, key=lambda x: (x.brand, x.model))

        if len(damaged_cars) <= count:
            repaired_cars = len(damaged_cars)
            for vehicle in ordered:
                vehicle.change_status()
                vehicle.recharge()

        else:
            repaired_cars = count
            for i in range(count):
                curr_vehicle = ordered[i]
                curr_vehicle.change_status()
                curr_vehicle.recharge()

        return f"{repaired_cars} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***"
        ordered_users = sorted(self.users, key=lambda x: -x.rating)
        for u in ordered_users:
            result += f"\n{str(u)}"

        return result
