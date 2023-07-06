from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Lidl", 2000)

    def test_initialization(self):
        self.assertEqual("Lidl", self.shopping_cart.shop_name)
        self.assertEqual(2000, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_raise_value_error_value_not_is_upper(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "ran3om"

        self.assertEqual(f"Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_raise_value_error_product_price_greater_or_equal_to_one_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("random", 100.0)

        self.assertEqual(f"Product random cost too much!", str(ve.exception))

    def test_add_to_cart_successfully(self):
        result = self.shopping_cart.add_to_cart("random", 90)

        self.assertEqual({"random": 90}, self.shopping_cart.products)
        self.assertEqual(f"random product was successfully added to the cart!", result)

    def test_remove_from_cart_product_name_in_products(self):
        self.shopping_cart.products = {"random": 90, "random2": 98}

        result = self.shopping_cart.remove_from_cart("random")

        self.assertEqual({"random2": 98}, self.shopping_cart.products)
        self.assertEqual(f"Product random was successfully removed from the cart!", result)

    def test_remove_from_shopping_cart_raise_error_product_name_not_in_products(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("random")

        self.assertEqual(f"No product with name random in the cart!", str(ve.exception))

    def test_add_method(self):
        other = ShoppingCart("Billa", 1000)

        self.shopping_cart.products = {"one": 1}
        other.products = {"two": 2}

        new_name = f"LidlBilla"
        new_budget = 3000
        new_products = {"one": 1, "two": 2}

        new_cart = ShoppingCart(new_name, new_budget)
        new_cart.products = new_products

        result = self.shopping_cart.__add__(other)

        self.assertEqual(new_cart.shop_name, result.shop_name)
        self.assertEqual(new_cart.budget, result.budget)
        self.assertEqual(new_cart.products, result.products)

    def test_buy_products_raise_error_total_sum_is_greater_than_budget(self):
        self.shopping_cart.products = {"random1": 500, "random2": 2000}

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with 500.00lv!", str(ve.exception))

    def test_buy_products_successfully(self):
        self.shopping_cart.products = {"random1": 20, "random2": 50}

        result = self.shopping_cart.buy_products()

        self.assertEqual(f"Products were successfully bought! Total cost: 70.00lv.", result)


if __name__ == "__main__":
    main()
