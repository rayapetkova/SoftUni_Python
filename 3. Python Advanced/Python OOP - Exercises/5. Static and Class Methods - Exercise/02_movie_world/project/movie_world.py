from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        curr_dvd = None

        for some_dvd in self.dvds:
            if some_dvd.id == dvd_id:
                curr_dvd = some_dvd

        for customer in self.customers:
            if customer.id == customer_id:
                if curr_dvd in customer.rented_dvds:
                    return f"{customer.name} has already rented {curr_dvd.name}"

                if curr_dvd.is_rented:
                    return f"DVD is already rented"

                if curr_dvd.age_restriction > customer.age:
                    return f"{customer.name} should be at least {curr_dvd.age_restriction} to rent this movie"

                curr_dvd.is_rented = True
                customer.rented_dvds.append(curr_dvd)
                return f"{customer.name} has successfully rented {curr_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        curr_dvd = None

        for some_dvd in self.dvds:
            if some_dvd.id == dvd_id:
                curr_dvd = some_dvd

        for customer in self.customers:
            if customer.id == customer_id:
                if curr_dvd in customer.rented_dvds:
                    customer.rented_dvds.remove(curr_dvd)
                    curr_dvd.is_rented = False
                    return f"{customer.name} has successfully returned {curr_dvd.name}"

                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        final = []

        for c in self.customers:
            final.append(str(c))

        for d in self.dvds:
            final.append(str(d))

        return '\n'.join(final)
