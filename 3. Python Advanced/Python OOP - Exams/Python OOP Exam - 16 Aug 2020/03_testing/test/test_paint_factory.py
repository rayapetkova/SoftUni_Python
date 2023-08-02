from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Random", 20)

    def test_initialization(self):
        self.assertEqual("Random", self.paint_factory.name)
        self.assertEqual(20, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_add_ingredient_product_in_valid_ingredients_and_can_add_and_type_not_in_ingredients(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        self.paint_factory.add_ingredient("red", 1)

        self.assertEqual({'white': 3, 'yellow': 3, 'blue': 3, 'red': 1}, self.paint_factory.ingredients)

    def test_add_ingredient_product_in_valid_ingredients_and_can_add_and_type_in_ingredients(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        self.paint_factory.add_ingredient("white", 1)

        self.assertEqual({'white': 4, 'yellow': 3, 'blue': 3}, self.paint_factory.ingredients)

    def test_add_ingredient_product_in_valid_ingredients_raise_value_error_but_can_not_add(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("white", 20)

        self.assertEqual(f"Not enough space in factory", str(ve.exception))

    def test_add_ingredient_raise_type_error_product_not_in_valid_ingredients(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("invalid colour", 2)

        self.assertEqual(f"Ingredient of type invalid colour not allowed in PaintFactory", str(te.exception))

    def test_remove_ingredient_product_in_ingredients_result_greater_than_zero(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        self.paint_factory.remove_ingredient("white", 2)

        self.assertEqual({'white': 1, 'yellow': 3, 'blue': 3}, self.paint_factory.ingredients)

    def test_remove_ingredient_product_in_ingredients_result_is_zero(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        self.paint_factory.remove_ingredient("white", 3)

        self.assertEqual({'white': 0, 'yellow': 3, 'blue': 3}, self.paint_factory.ingredients)

    def test_remove_ingredient_product_in_ingredients_raise_value_error_result_less_than_zero(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("white", 4)

        self.assertEqual(f"Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_raise_key_error_product_not_in_ingredients(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("invalid", 2)

        self.assertEqual(f"'No such ingredient in the factory'", str(ke.exception))

    def test_product_return(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        self.assertEqual({'white': 3, 'yellow': 3, 'blue': 3}, self.paint_factory.products)

    def test_repr_method(self):
        self.paint_factory.ingredients = {'white': 3, 'yellow': 3, 'blue': 3}

        expected = f"Factory name: Random with capacity 20.\n" \
                   f"white: 3\nyellow: 3\nblue: 3\n"

        self.assertEqual(expected, str(self.paint_factory))


if __name__ == "__main__":
    main()
