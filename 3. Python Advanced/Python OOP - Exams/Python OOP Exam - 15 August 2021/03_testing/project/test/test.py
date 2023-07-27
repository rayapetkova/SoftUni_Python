from project.pet_shop import PetShop
from unittest import TestCase, main


class TestsPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Random')

    def test_initialization(self):
        self.assertEqual('Random', self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_method_raise_error_quantity_less_than_equal_to_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food('first', 0)

        self.assertEqual(f'Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_method_name_not_in_food(self):
        self.pet_shop.food = {'first': 20, 'second': 30}

        result = self.pet_shop.add_food('third', 40)

        self.assertEqual({'first': 20, 'second': 30, 'third': 40}, self.pet_shop.food)
        self.assertEqual(f"Successfully added 40.00 grams of third.", result)

    def test_add_method_name_in_food(self):
        self.pet_shop.food = {'first': 20, 'second': 30}

        result = self.pet_shop.add_food('second', 100)

        self.assertEqual({'first': 20, 'second': 130}, self.pet_shop.food)
        self.assertEqual(f"Successfully added 100.00 grams of second.", result)

    def test_add_pet_name_not_in_pets(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']

        result = self.pet_shop.add_pet('pig')

        self.assertEqual(['dog', 'cat', 'parrot', 'pig'], self.pet_shop.pets)
        self.assertEqual(f"Successfully added pig.", result)

    def test_add_pet_raise_exception_name_in_pets(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']

        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('dog')

        self.assertEqual(f"Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_raise_exception_name_not_in_pets(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']

        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('idk', 'random')

        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_not_in_food_list(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']
        self.pet_shop.food = {'first': 20, 'second': 30}

        result = self.pet_shop.feed_pet('random', 'dog')

        self.assertEqual(f'You do not have random', result)

    def test_feed_pet_quantity_less_than_one_hundred(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']
        self.pet_shop.food = {'first': 20, 'second': 30}

        result = self.pet_shop.feed_pet('first', 'dog')

        self.assertEqual({'first': 1020, 'second': 30}, self.pet_shop.food)
        self.assertEqual(f"Adding food...", result)

    def test_feed_pet_successfully(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']
        self.pet_shop.food = {'first': 200, 'second': 30}

        result = self.pet_shop.feed_pet('first', 'dog')

        self.assertEqual({'first': 100, 'second': 30}, self.pet_shop.food)
        self.assertEqual(f"dog was successfully fed", result)

    def test_repr_method(self):
        self.pet_shop.pets = ['dog', 'cat', 'parrot']

        self.assertEqual(f'Shop Random:\nPets: dog, cat, parrot', str(self.pet_shop))


if __name__ == "__main__":
    main()
