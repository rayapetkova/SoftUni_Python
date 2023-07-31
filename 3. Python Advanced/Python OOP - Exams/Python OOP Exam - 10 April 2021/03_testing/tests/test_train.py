from project.train.train import Train
from unittest import TestCase, main


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Random", 5)

    def test_initialization(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

        self.assertEqual("Random", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_method_raise_value_error_len_passengers_equal_to_capacity(self):
        self.train.passengers = ['1', '2', '3', '4', '5']

        with self.assertRaises(ValueError) as ve:
            self.train.add('6')

        self.assertEqual("Train is full", str(ve.exception))

    def test_add_method_raise_value_error_name_in_passengers(self):
        self.train.passengers = ['1', '2', '3', '4']

        with self.assertRaises(ValueError) as ve:
            self.train.add('1')

        self.assertEqual("Passenger 1 Exists", str(ve.exception))

    def test_add_method_successfully(self):
        self.train.passengers = ['1', '2', '3', '4']

        result = self.train.add('5')

        self.assertEqual(['1', '2', '3', '4', '5'], self.train.passengers)
        self.assertEqual("Added passenger 5", result)

    def test_remove_method_name_not_in_passengers(self):
        self.train.passengers = ['1', '2', '3', '4']

        with self.assertRaises(ValueError) as ve:
            self.train.remove('5')

        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_method_successfully(self):
        self.train.passengers = ['1', '2', '3', '4']

        result = self.train.remove('1')

        self.assertEqual(['2', '3', '4'], self.train.passengers)
        self.assertEqual("Removed 1", result)


if __name__ == "__main__":
    main()
