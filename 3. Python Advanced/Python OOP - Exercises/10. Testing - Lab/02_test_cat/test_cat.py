from unittest import TestCase, main
from test_cat_code import Cat  # This line needs to be commented if submitting to judge


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Kate")

    def test_initialization(self):
        self.assertEqual("Kate", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_fed_cat_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_cannot_eat_if_already_fed_cat_raise_an_error(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(f"Already fed.", str(ex.exception))

    def test_cannot_fall_asleep_if_not_fed_raise_an_error(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    main()