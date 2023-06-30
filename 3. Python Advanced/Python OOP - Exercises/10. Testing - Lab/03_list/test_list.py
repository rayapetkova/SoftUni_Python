from unittest import TestCase, main
from list_code import IntegerList  # This line needs to be commented if submitting to judge


class TestList(TestCase):
    def setUp(self) -> None:
        self.numbers_list = IntegerList(1, 4.5, 3, True, 10)

    def test_initialization(self):
        result = self.numbers_list.get_data()
        expected = [1, 3, 10]
        self.assertEqual(expected, result)

    def test_add_a_non_integer_element_raise_error(self):
        element = 2.4

        with self.assertRaises(ValueError) as ve:
            self.numbers_list.add(element)

        self.assertEqual(f"Element is not Integer", str(ve.exception))

    def test_add_an_integer_element_and_return_the_list(self):
        element = 5
        expected = [1, 3, 10, 5]
        result = self.numbers_list.add(element)

        self.assertEqual(expected, result)

    def test_removing_index_out_of_range_raise_error(self):
        idx = 3

        with self.assertRaises(IndexError) as ie:
            self.numbers_list.remove_index(idx)

        self.assertEqual(f"Index is out of range", str(ie.exception))

    def test_removing_valid_index(self):
        idx = 1
        self.assertEqual(3, self.numbers_list.get_data()[idx])
        self.numbers_list.remove_index(idx)

    def test_get_method_index_out_of_range_raise_error(self):
        idx = 3

        with self.assertRaises(IndexError) as ie:
            self.numbers_list.get(idx)

        self.assertEqual(f"Index is out of range", str(ie.exception))

    def test_get_method_and_return_element_on_valid_index(self):
        idx = 1
        result = self.numbers_list.get(idx)
        self.assertEqual(3, result)

    def test_insert_method_index_out_of_range_raise_error(self):
        idx = 3

        with self.assertRaises(IndexError) as ie:
            self.numbers_list.insert(idx, 5)

        self.assertEqual(f"Index is out of range", str(ie.exception))

    def test_insert_method_element_is_not_an_integer_raise_error(self):
        element = "number"

        with self.assertRaises(ValueError) as ve:
            self.numbers_list.insert(1, element)

        self.assertEqual(f"Element is not Integer", str(ve.exception))

    def test_insert_method_with_valid_index_and_valid_element(self):
        idx, element = 2, 5
        self.numbers_list.insert(idx, element)
        self.assertEqual([1, 3, 5, 10], self.numbers_list.get_data())

    def test_get_biggest_number(self):
        result = self.numbers_list.get_biggest()
        self.assertEqual(10, result)

    def test_get_index_of_element(self):
        element = 3
        result = self.numbers_list.get_index(element)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()