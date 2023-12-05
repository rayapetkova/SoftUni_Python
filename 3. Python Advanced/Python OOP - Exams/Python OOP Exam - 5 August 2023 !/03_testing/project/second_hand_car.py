class SecondHandCar:
    def __init__(self, model: str, car_type: str, mileage: int, price: float):
        self.model = model
        self.car_type = car_type
        self.mileage = mileage
        self.price = price
        self.repairs = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 1.0:
            raise ValueError('Price should be greater than 1.0!')
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value <= 100:
            raise ValueError('Please, second-hand cars only! Mileage must be greater than 100!')
        self._mileage = value

    def set_promotional_price(self, new_price: float):
        if new_price >= self.price:
            raise ValueError('You are supposed to decrease the price!')
        self.price = new_price
        return 'The promotional price has been successfully set.'

    def need_repair(self, repair_price: float, repair_description: str):
        if repair_price > self.price / 2:
            return 'Repair is impossible!'
        self.price += repair_price
        self.repairs.append(repair_description)
        return f'Price has been increased due to repair charges.'

    def __gt__(self, other):
        if self.car_type != other.car_type:
            return 'Cars cannot be compared. Type mismatch!'
        return self.price > other.price

    def __str__(self):
        return f"""Model {self.model} | Type {self.car_type} | Milage {self.mileage}km
Current price: {self.price:.2f} | Number of Repairs: {len(self.repairs)}"""

