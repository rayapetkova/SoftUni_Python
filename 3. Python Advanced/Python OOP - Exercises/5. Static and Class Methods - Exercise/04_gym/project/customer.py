class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id

    @staticmethod
    def get_next_id():
        upcoming_customer = Customer.id
        Customer.id += 1
        return upcoming_customer

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
