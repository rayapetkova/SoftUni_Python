from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduce_percents = round((mileage / self.max_mileage) * 100)

        self.battery_level -= reduce_percents
