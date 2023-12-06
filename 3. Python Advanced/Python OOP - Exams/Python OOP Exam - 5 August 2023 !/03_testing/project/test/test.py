from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class SecondHandCarTests(TestCase):
    
    def setUp(self) -> None:
        self.car = SecondHandCar('Random', 'TestType', 1000, 5000)

    def test_initialization(self):
        self.assertEqual('Random', self.car.model)
        self.assertEqual('TestType', self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(5000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_raise_value_error_value_less_than_or_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_raise_value_error_value_less_than_or_equal_to_one_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual(f'Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_method_raise_value_error_new_greater_than_or_equal_to_self_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(5000)

        self.assertEqual(f'You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_method_successfully(self):
        result = self.car.set_promotional_price(4000)

        self.assertEqual(4000, self.car.price)
        self.assertEqual(f'The promotional price has been successfully set.', result)

    def test_need_repair_method_impossible_repair_price_greater_than_half_of_self_price(self):
        result = self.car.need_repair(2600, 'something')

        self.assertEqual(f'Repair is impossible!', result)

    def test_need_repair_method_successfully(self):
        self.car.repairs = ['first', 'second', 'third']

        result = self.car.need_repair(2000, 'forth')

        self.assertEqual(7000, self.car.price)
        self.assertEqual(['first', 'second', 'third', 'forth'], self.car.repairs)
        self.assertEqual(f'Price has been increased due to repair charges.', result)

    def test__gt__method_car_type_different_than_other_car_type(self):
        other = SecondHandCar('idk', 'invalid', 2000, 4000)

        result = self.car.__gt__(other)

        self.assertEqual(f'Cars cannot be compared. Type mismatch!', result)

    def test__gt__method_self_price_more_than_other_price(self):
        other = SecondHandCar('idk', 'TestType', 2000, 4000)

        result = self.car.__gt__(other)

        self.assertEqual(True, result)

    def test__gt__method_self_price_less_than_other_price(self):
        other = SecondHandCar('idk', 'TestType', 2000, 6000)

        result = self.car.__gt__(other)

        self.assertEqual(False, result)

    def test__str__method(self):
        self.car.repairs = ['first', 'second', 'third']

        self.assertEqual(f"""Model Random | Type TestType | Milage 1000km
Current price: 5000.00 | Number of Repairs: 3""", str(self.car))


if __name__ == '__main__':
    main()
