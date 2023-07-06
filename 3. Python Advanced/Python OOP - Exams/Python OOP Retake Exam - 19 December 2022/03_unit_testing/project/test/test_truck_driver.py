from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("TestName", 4.0)

    def test_initialization(self):
        self.assertEqual("TestName", self.driver.name)
        self.assertEqual(4.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_method_raise_exception_value_is_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -20

        self.assertEqual(f"TestName went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_raise_exception_cargo_location_already_in_available_cargos(self):
        self.driver.available_cargos = {"First": 20, "Second": 34}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("First", 40)

        self.assertEqual(f"Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_method(self):
        self.driver.available_cargos = {"Second": 34, "Third": 27}

        result = self.driver.add_cargo_offer("First", 40)

        self.assertEqual({"Second": 34, "Third": 27, "First": 40}, self.driver.available_cargos)
        self.assertEqual(f"Cargo for 40 to First was added as an offer.", result)

    def test_drive_best_cargo_offer_catch_error_empty_dictionary(self):
        self.assertEqual(f"There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_drive_best_cargo_offer(self):
        self.driver.available_cargos = {"Second": 40, "First": 60}

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(240.0, self.driver.earned_money)
        self.assertEqual(60, self.driver.miles)
        self.assertEqual(f"TestName is driving 60 to First.", result)

    def test_check_for_activities_method(self):
        self.driver.earned_money = 10_000

        self.driver.check_for_activities(250)
        self.assertEqual(9980, self.driver.earned_money)

        self.driver.earned_money = 10_000

        self.driver.check_for_activities(1000)
        self.assertEqual(9875, self.driver.earned_money)

        self.driver.earned_money = 10_000

        self.driver.check_for_activities(1500)
        self.assertEqual(9335, self.driver.earned_money)

        self.driver.earned_money = 100_000

        self.driver.check_for_activities(10_000)
        self.assertEqual(88250, self.driver.earned_money)

    def test_repr_method(self):
        self.assertEqual(f"TestName has 0 miles behind his back.", str(self.driver))


if __name__ == "__main__":
    main()
