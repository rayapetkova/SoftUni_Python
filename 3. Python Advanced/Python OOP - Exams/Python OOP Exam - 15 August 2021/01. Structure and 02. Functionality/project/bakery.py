from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_TYPES_FOOD = {
        'Bread': Bread,
        'Cake': Cake
    }

    VALID_TYPES_DRINKS = {
        'Tea': Tea,
        'Water': Water
    }

    VALID_TYPES_TABLES = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        curr_food = Bakery.VALID_TYPES_FOOD[food_type](name, price)
        self.food_menu.append(curr_food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        curr_drink = Bakery.VALID_TYPES_DRINKS[drink_type](name, portion, brand)
        self.drinks_menu.append(curr_drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_name: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        curr_table = Bakery.VALID_TYPES_TABLES[table_name](table_number, capacity)
        self.tables_repository.append(curr_table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]

        if not table:
            return f"Could not find table {table_number}"

        curr_table = table[0]

        not_available = []
        ordered = []

        for food_name in args:
            curr_food = [f for f in self.food_menu if f.name == food_name]

            if not curr_food:
                not_available.append(food_name)
            else:
                curr_table.order_food(curr_food[0])
                ordered.append(curr_food[0].__repr__())

        final = [f"Table {table_number} ordered:"]

        for order in ordered:
            final.append(order)

        final.append(f"{self.name} does not have in the menu:")

        for unavailable in not_available:
            final.append(unavailable)

        return '\n'.join(final)

    def order_drink(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]

        if not table:
            return f"Could not find table {table_number}"

        curr_table = table[0]

        not_available = []
        ordered = []

        for drink_name in args:
            curr_drink = [d for d in self.drinks_menu if d.name == drink_name]

            if not curr_drink:
                not_available.append(drink_name)
            else:
                curr_table.order_food(curr_drink[0])
                ordered.append(curr_drink[0].__repr__())

        final = [f"Table {table_number} ordered:"]

        for order in ordered:
            final.append(order)

        final.append(f"{self.name} does not have in the menu:")

        for unavailable in not_available:
            final.append(unavailable)

        return '\n'.join(final)

    def leave_table(self, table_number: int):
        curr_table = [t for t in self.tables_repository if t.table_number == table_number][0]
        bill = curr_table.get_bill()
        self.total_income += bill

        curr_table.clear()

        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        final = []

        for table in self.tables_repository:
            if not table.number_of_people:
                final.append(table.free_table_info())

        return '\n'.join(final)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
