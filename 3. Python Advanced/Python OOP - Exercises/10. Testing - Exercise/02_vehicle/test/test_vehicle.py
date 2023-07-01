from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100.0, 200.0)

    def test_initialization(self):
        self.assertEqual(100.0, self.vehicle.fuel)
        self.assertEqual(100.0, self.vehicle.capacity)
        self.assertEqual(200.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_method_raise_exception_if_fuel_is_lower_than_fuel_needed(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(200)

        self.assertEqual(f"Not enough fuel", str(ex.exception))

    def test_drive_method_with_fuel_greter_than_needed_fuel(self):
        self.vehicle.drive(50)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_method_raise_exception_if_current_fuel_plus_fuel_is_greater_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(30)

        self.assertEqual(f"Too much fuel", str(ex.exception))

    def test_refuel_method_increase_fuel(self):
        self.vehicle.fuel = 40
        self.vehicle.refuel(30)
        self.assertEqual(70, self.vehicle.fuel)

    def test_str_method(self):
        self.assertEqual(f"The vehicle has 200.0 horse "
                         f"power with 100.0 fuel left and 1.25 fuel consumption", str(self.vehicle))