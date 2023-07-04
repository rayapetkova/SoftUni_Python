from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_initialization(self):
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_raise_exception_shelf_not_in_toy_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "Bear")

        self.assertEqual(f"Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_raise_exception_toy_is_already_on_shelf(self):
        self.toy_store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Bear")

        self.assertEqual(f"Toy is already in shelf!", str(ex.exception))

    def test_add_toy_raise_exception_shelf_is_already_taken(self):
        self.toy_store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Second")

        self.assertEqual(f"Shelf is already taken!", str(ex.exception))

    def test_add_toy(self):
        result = self.toy_store.add_toy("A", "Bear")

        self.assertEqual("Bear", self.toy_store.toy_shelf["AD"])
        self.assertEqual(f"Toy:Bear placed successfully!", result)

    def test_remove_toy_raise_exception_shelf_not_in_toy_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "Bear")

        self.assertEqual(f"Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_raise_exception_toy_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Bear")

        self.assertEqual(f"Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy(self):
        self.toy_store.toy_shelf["A"] = "Bear"

        result = self.toy_store.remove_toy("A", "Bear")

        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual(f"Remove toy:Bear successfully!", result)


if __name__ == "__main__":
    main()
