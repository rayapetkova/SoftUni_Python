from project1.client import Client
from project1.meals.meal import Meal
from project1.meals.starter import Starter
from project1.meals.main_dish import MainDish
from project1.meals.dessert import Dessert


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception(f"The client has already been registered!")

        curr_client = Client(client_phone_number)
        self.clients_list.append(curr_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if not meal.__class__.__name__ == "Starter" and not meal.__class__.__name__ == "MainDish" and not meal.__class__.__name__ == "Dessert":
                continue

            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")

        final = []

        for meal in self.menu:
            final.append(meal.details())

        return "\n".join(final)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # {'Wild Mushrooms': 20}
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")

        client = [c for c in self.clients_list if c.phone_number == client_phone_number]

        if not client:
            self.register_client(client_phone_number)

        curr_client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        adding_meals = []
        for meal in meal_names_and_quantities.keys():
            c_meal = [m for m in self.menu if m.name == meal]

            if not c_meal:
                raise Exception(f"{meal} is not on the menu!")

            curr_meal = c_meal[0]

            if meal_names_and_quantities[meal] > curr_meal.quantity:
                raise Exception(f"Not enough quantity of {curr_meal.__class__.__name__}: {meal}!")

            adding_meals.append(curr_meal)

        for meal in adding_meals:
            curr_client.shopping_cart.append(meal)
            increase_bill = meal.price * meal_names_and_quantities[meal.name]

            meal.quantity -= meal_names_and_quantities[meal.name]
            curr_client.bill += increase_bill

        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in curr_client.shopping_cart])} for {curr_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        curr_client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not curr_client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        for c_meal in curr_client.shopping_cart:
            for meal in self.menu:
                if c_meal.name == meal.name:
                    meal.quantity += c_meal.quantity

        curr_client.shopping_cart = []
        curr_client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        curr_client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not curr_client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        paid_money = curr_client.bill

        curr_client.shopping_cart = []
        curr_client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


# food_orders_app = FoodOrdersApp()
# print(food_orders_app.register_client("0899999999"))
# french_toast = Starter("French toast", 6.50, 5)
# hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
# tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
# risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
# chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
# chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
# print(food_orders_app.add_meals_to_menu(
#     french_toast, hummus_and_avocado_sandwich,
#     tortilla_with_beef_and_pork,
#     risotto_with_wild_mushrooms,
#     chocolate_cake_with_mascarpone,
#     chocolate_and_violets))
# print(food_orders_app.show_menu())
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)

