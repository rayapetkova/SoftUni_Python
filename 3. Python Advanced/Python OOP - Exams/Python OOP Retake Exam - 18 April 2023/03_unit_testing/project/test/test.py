from project.robot import Robot
from unittest import TestCase, main


class RobotTests(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1", "Education", 50, 500)

    def test_initialization(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(500, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_raise_value_error_value_not_in_allowed_categories(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid category"

        self.assertEqual(f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_setter_raise_value_error_value_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -20

        self.assertEqual(f"Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_hardware_component_in_hardware_upgrades(self):
        self.robot.hardware_upgrades = ["Random component"]

        result = self.robot.upgrade("Random component", 60)

        self.assertEqual(f"Robot 1 was not upgraded.", result)

    def test_upgrade_method_hardware_component_not_in_hardware_upgrades(self):
        result = self.robot.upgrade("Random component", 60)

        self.assertEqual(["Random component"], self.robot.hardware_upgrades)
        self.assertEqual(590, self.robot.price)
        self.assertEqual(f"Robot 1 was upgraded with Random component.", result)

    def test_update_method_software_updates_version_is_lower_or_equal_to_max_software_updates(self):
        self.robot.software_updates = [1, 3, 10]

        result = self.robot.update(8, 30)

        self.assertEqual(f"Robot 1 was not updated.", result)

    def test_update_method_available_capacity_less_than_needed_capacity(self):
        result = self.robot.update(10, 70)

        self.assertEqual(f"Robot 1 was not updated.", result)

    def test_update_method(self):
        result = self.robot.update(9, 20)

        self.assertEqual([9], self.robot.software_updates)
        self.assertEqual(30, self.robot.available_capacity)
        self.assertEqual(f"Robot 1 was updated to version 9.", result)

    def test_gt_method_price_greater_than_other_price(self):
        other = Robot("2", "Education", 40, 400)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 1 is more expensive than Robot with ID 2.", result)

    def test_gt_method_price_equal_to_other_price(self):
        other = Robot("2", "Education", 40, 500)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 1 costs equal to Robot with ID 2.", result)

    def test_gt_method_price_less_than_other_price(self):
        other = Robot("2", "Education", 40, 600)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 1 is cheaper than Robot with ID 2.", result)


if __name__ == "__main__":
    main()
