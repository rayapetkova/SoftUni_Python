from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError(f"Brand cannot be empty!")

        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError(f"Model cannot be empty!")
        
        self.__model = value
    
    @property
    def license_plate_number(self):
        return self.__license_plate_number
    
    @license_plate_number.setter
    def license_plate_number(self, value):
        if not value.strip():
            raise ValueError(f"License plate number is required!")

        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        status = "OK" if not self.is_damaged else "Damaged"
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {status}"
