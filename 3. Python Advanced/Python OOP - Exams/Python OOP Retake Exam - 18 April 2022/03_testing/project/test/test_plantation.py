from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(3)

    def test_size_raise_error_value_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -20

        self.assertEqual(f"Size must be positive number!", str(ve.exception))

    def test_hire_worker_raise_error_worker_already_in_workers(self):
        self.plantation.workers = ['first', 'second', 'third']

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('first')

        self.assertEqual(f"Worker already hired!", str(ve.exception))

    def test_hire_worker_successfully(self):
        self.plantation.workers = ['first', 'second', 'third']

        result = self.plantation.hire_worker('forth')

        self.assertEqual(self.plantation.workers, ['first', 'second', 'third', 'forth'])
        self.assertEqual(f"forth successfully hired.", result)

    def test_len_method(self):
        self.plantation.plants = {'first': ['plant1', 'plant2'], 'second': ['plant3', 'plant4']}

        result = len(self.plantation)

        self.assertEqual(4, result)

    def test_planting_raise_error_worker_not_in_workers(self):
        self.plantation.workers = ['first', 'second', 'third']

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('forth', 'plant1')

        self.assertEqual(f"Worker with name forth is not hired!", str(ve.exception))

    def test_planting_raise_error_plants_more_than_size(self):
        self.plantation.workers = ['first', 'second', 'third']
        self.plantation.plants = {'first': ['plant1', 'plant2'], 'second': ['plant3', 'plant4']}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('first', 'one_more_plant')

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_in_plants_keys(self):
        self.plantation.size = 20
        self.plantation.workers = ['first', 'second', 'third']
        self.plantation.plants = {'first': ['plant1', 'plant2'], 'second': ['plant3', 'plant4']}

        result = self.plantation.planting('first', 'one_more_plant')

        self.assertEqual({'first': ['plant1', 'plant2', 'one_more_plant'], 'second': ['plant3', 'plant4']},
                         self.plantation.plants)
        self.assertEqual(f"first planted one_more_plant.", result)

    def test_planting_worker_not_in_plants_keys(self):
        self.plantation.size = 20
        self.plantation.workers = ['first', 'second', 'third']
        self.plantation.plants = {'first': ['plant1', 'plant2'], 'second': ['plant3', 'plant4']}

        result = self.plantation.planting('third', 'one_plant')

        self.assertEqual({'first': ['plant1', 'plant2'], 'second': ['plant3', 'plant4'], 'third': ['one_plant']},
                         self.plantation.plants)
        self.assertEqual(f"third planted it's first one_plant.", result)

    def test_str_method(self):
        self.plantation.size = 20
        self.plantation.workers = ['first', 'second', 'third']
        self.plantation.plants = {'first': ['plant1', 'plant2'], 'second': ['plant3', 'plant4'], 'third': ['one_plant']}

        result = self.plantation.__str__()

        actual = f"Plantation size: 20\nfirst, second, third\nfirst planted: plant1, plant2\n" \
                 f"second planted: plant3, plant4\nthird planted: one_plant"

        self.assertEqual(actual, result)

    def test_repr_method(self):
        self.plantation.workers = ['first', 'second', 'third']

        result = self.plantation.__repr__()

        actual = f'Size: 3\nWorkers: first, second, third'

        self.assertEqual(actual, result)


if __name__ == '__main__':
    main()
