from project.robot import Robot
from unittest import TestCase, main


class RobotTests(TestCase):
    def setUp(self) -> None:
        self.robot = Robot('1', 'Education', 20, 6000)

    def test_initialization(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

        self.assertEqual('1', self.robot.robot_id)
        self.assertEqual('Education', self.robot.category)
        self.assertEqual(20, self.robot.available_capacity)
        self.assertEqual(6000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_raise_value_error_value_not_in_allowed_categories(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Invalid'

        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_price_setter_raise_value_error_value_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -20

        self.assertEqual(f"Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_hardware_component_in_hardware_upgrades(self):
        self.robot.hardware_upgrades = ['first', 'second', 'third']

        result = self.robot.upgrade('first', 300)

        self.assertEqual(f"Robot 1 was not upgraded.", result)

    def test_upgrade_method_successfully(self):
        self.robot.hardware_upgrades = ['first', 'second', 'third']

        result = self.robot.upgrade('forth', 300)

        self.assertEqual(['first', 'second', 'third', 'forth'], self.robot.hardware_upgrades)
        self.assertEqual(6450, self.robot.price)
        self.assertEqual(f"Robot 1 was upgraded with forth.", result)

    def test_update_method_software_updates_and_version_less_than_max_robot_not_updated(self):
        self.robot.software_updates = [10, 20, 30]

        result = self.robot.update(30, 10)

        self.assertEqual(f"Robot 1 was not updated.", result)

    def test_update_method_available_capacity_less_than_needed_capacity(self):
        result = self.robot.update(20, 30)

        self.assertEqual(f"Robot 1 was not updated.", result)

    def test_update_method_successfully(self):
        self.robot.software_updates = [10, 20, 30]

        result = self.robot.update(40, 10)

        self.assertEqual([10, 20, 30, 40], self.robot.software_updates)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(f"Robot 1 was updated to version 40.", result)

    def test__gt__method_self_price_greater_than_other_price(self):
        other = Robot('2', 'Education', 10, 5000)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 1 is more expensive than Robot with ID 2.", result)

    def test__gt__method_self_price_equal_to_other_price(self):
        other = Robot('2', 'Education', 10, 6000)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 1 costs equal to Robot with ID 2.", result)

    def test__gt__method_self_price_less_than_other_price(self):
        other = Robot('2', 'Education', 10, 7000)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 1 is cheaper than Robot with ID 2.", result)


if __name__ == "__main__":
    main()