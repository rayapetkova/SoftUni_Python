class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, new_quantity: int):
        if self.quantity + new_quantity <= self.size:
            self.quantity += new_quantity

    def status(self):
        return self.size - self.quantity


# Test code:

# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())
