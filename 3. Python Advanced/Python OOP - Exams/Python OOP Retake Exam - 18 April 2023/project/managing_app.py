from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        curr_user = User(first_name, last_name, driving_license_number)
        self.users.append(curr_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ['PassengerCar', 'CargoVan']:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        all_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
        curr_vehicle = all_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(curr_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True

        curr_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(curr_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        curr_user, curr_vehicle, curr_route = None, None, None

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                if user.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                curr_user = user

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                if vehicle.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
                curr_vehicle = vehicle

        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                curr_route = route

        curr_vehicle.drive(curr_route.length)

        if is_accident_happened:
            curr_vehicle.is_damaged = True
            curr_user.decrease_rating()

        else:
            curr_user.increase_rating()

        status = "OK" if not curr_vehicle.is_damaged else "Damaged"
        return f"{curr_vehicle.brand} {curr_vehicle.model} License plate: {license_plate_number} Battery: {curr_vehicle.battery_level}% Status: {status}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([v for v in self.vehicles if v.is_damaged], key=lambda x: (x.brand, x.model))
        first_count_vehicles = damaged_vehicles[:count]

        for v in first_count_vehicles:
            v.is_damaged = False
            v.battery_level = 100

        return f"{len(first_count_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted([u for u in self.users], key=lambda x: -x.rating)
        final = ["*** E-Drive-Rent ***"]

        for c_user in sorted_users:
            final.append(str(c_user))

        return "\n".join(u for u in final)