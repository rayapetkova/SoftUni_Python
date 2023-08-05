from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    loans_granted = []

    VALID_LOANS = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }

    VALID_CLIENTS = {
        'Student': Student,
        'Adult': Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.VALID_LOANS.keys():
            raise Exception(f"Invalid loan type!")

        curr_loan = BankApp.VALID_LOANS[loan_type]()
        self.loans.append(curr_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_CLIENTS.keys():
            raise Exception(f"Invalid client type!")

        if len(self.clients) == self.capacity:
            return f"Not enough bank capacity."

        curr_client = BankApp.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(curr_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        curr_loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
        curr_client = [c for c in self.clients if c.client_id == client_id][0]

        if (curr_loan.__class__.__name__ == "MortgageLoan" and curr_client.__class__.__name__ == "Student") or \
                (curr_loan.__class__.__name__ == "StudentLoan" and curr_client.__class__.__name__ == "Adult"):
            raise Exception(f"Inappropriate loan type!")

        self.loans.remove(curr_loan)
        curr_client.loans.append(curr_loan)
        BankApp.loans_granted.append(curr_loan)

        return f"Successfully granted {loan_type} to {curr_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id]

        if not client:
            raise Exception(f"No such client!")
        curr_client = client[0]

        if curr_client.loans:
            raise Exception(f"The client has loans! Removal is impossible!")

        self.clients.remove(curr_client)
        return f"Successfully removed {curr_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        average_client_interest_rate = 0
        if self.clients:
            average_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)

        return f"Active Clients: {len(self.clients)}\nTotal Income: {sum([c.income for c in self.clients]):.2f}\n" \
               f"Granted Loans: {len(BankApp.loans_granted)}, Total Sum: {sum([l.amount for l in BankApp.loans_granted]):.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n" \
               f"Average Client Interest Rate: {average_client_interest_rate:.2f}"


# bank = BankApp(3)
#
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
#
#
# print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
# print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
# print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
# print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
#
# print(bank.grant_loan('StudentLoan', '1234567891'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
#
# print(bank.remove_client('1234567999'))
#
# print(bank.increase_loan_interest('StudentLoan'))
# print(bank.increase_loan_interest('MortgageLoan'))
#
# print(bank.increase_clients_interest(1.2))
# print(bank.increase_clients_interest(3.5))
#
# print(bank.get_statistics())
