class Robot:
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def __init__(self, robot_id: str, category: str, capacity: int, price: float):
        self.robot_id = robot_id
        self.category = category
        self.available_capacity = capacity
        self.price = price
        self.hardware_upgrades = []
        self.software_updates = []

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Category should be one of '{self.ALLOWED_CATEGORIES}'")
        self.__category = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

    def upgrade(self, hardware_component: str, component_price: float):
        if hardware_component in self.hardware_upgrades:
            return f"Robot {self.robot_id} was not upgraded."
        self.hardware_upgrades.append(hardware_component)
        self.price += component_price * self.PRICE_INCREMENT
        return f'Robot {self.robot_id} was upgraded with {hardware_component}.'

    def update(self, version: float, needed_capacity: int):
        if (self.software_updates and version <= max(self.software_updates)) or self.available_capacity < needed_capacity:
            return f"Robot {self.robot_id} was not updated."
        self.software_updates.append(version)
        self.available_capacity -= needed_capacity
        return f'Robot {self.robot_id} was updated to version {version}.'

    def __gt__(self, other):
        if self.price > other.price:
            return f'Robot with ID {self.robot_id} is more expensive than Robot with ID {other.robot_id}.'
        if self.price == other.price:
            return f'Robot with ID {self.robot_id} costs equal to Robot with ID {other.robot_id}.'
        return f'Robot with ID {self.robot_id} is cheaper than Robot with ID {other.robot_id}.'


