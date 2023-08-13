class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not (value[0] == "0" and len(value) == 10 and value.isdigit()):
            raise ValueError(f"Invalid phone number!")

        self.__phone_number = value
