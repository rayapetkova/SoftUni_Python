from unittest import TestCase, main
from car_manager_code import Car  # # This line needs to be commented if submitting to judge


class CarTests(TestCase):
    def setUp(self) -> None:
        self.car = Car("TestMake", "TestModel", 50, 100)

    def test_initialization(self):
        self.assertEqual("TestMake", self.car.make)
        self.assertEqual("TestModel", self.car.model)
        self.assertEqual(50, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raise_exception_if_not_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "TestModel", 50, 100)

        self.assertEqual(f"Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raise_exception_if_not_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("TestMake", "", 50, 100)

        self.assertEqual(f"Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_raise_exception_if_value_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("TestMake", "TestModel", 0, 100)

        self.assertEqual(f"Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_raise_exception_if_value_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("TestMake", "TestModel", 50, 0)

        self.assertEqual(f"Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_raise_exception_if_value_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -3

        self.assertEqual(f"Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raise_exception_if_fuel_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual(f"Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_with_greater_fuel_than_the_capacity(self):
        fuel = 105
        self.car.refuel(fuel)
        self.assertEqual(100, self.car.fuel_amount)

    def test_refuel_method_with_valid_fuel(self):
        fuel = 98
        self.car.refuel(fuel)
        self.assertEqual(98, self.car.fuel_amount)

    def test_drive_method_raise_exception_if_needed_is_greater_than_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        self.assertEqual(f"You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_with_needed_lower_than_fuel_amount(self):
        self.car.fuel_amount = 50
        self.car.drive(50)
        self.assertEqual(25, self.car.fuel_amount)


if __name__ == "__main__":
    main()
