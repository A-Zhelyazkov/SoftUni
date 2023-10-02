from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }
    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        loan = [l for l in self.loans if loan_type == l.__class__.__name__][0]
        client = [c for c in self.clients if c.client_id == client_id][0]

        if isinstance(loan, StudentLoan) and isinstance(client, Student):
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        elif isinstance(loan, MortgageLoan) and isinstance(client, Adult):
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id]

        if not client:
            raise Exception("No such client!")

        c = client[0]
        if c.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(c)
        return f"Successfully removed {c.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        if loan_type == "StudentLoan":
            loans = [l for l in self.loans if isinstance(l, StudentLoan)]
            for l in loans:
                l.increase_interest_rate()
        elif loan_type == "MortgageLoan":
            loans = [l for l in self.loans if isinstance(l, MortgageLoan)]
            for l in loans:
                l.increase_interest_rate()

        count = len(loans)
        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate):
        clients = [c for c in self.clients if c.interest < min_rate]
        for c in clients:
            c.increase_clients_interest()

        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self):
        total_income = 0
        loaned_sum = 0
        granted_loans = 0
        not_granted_sum = 0
        total_interest_rate = 0
        for c in self.clients:
            total_income += c.income
            if c.loans:
                granted_loans += len(c.loans)
                for l in c.loans:
                    loaned_sum += l.amount

        for l in self.loans:
            not_granted_sum += l.amount

        for c in self.clients:
            total_interest_rate += c.interest

        if self.clients:
            average_rate = total_interest_rate / len(self.clients)
        else:
            average_rate = 0

        return f"Active Clients: {len(self.clients)}\n" \
                 f"Total Income: {total_income:.2f}\n" \
                 f"Granted Loans: {granted_loans}, Total Sum: {loaned_sum:.2f}\n" \
                 f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
                 f"Average Client Interest Rate: {average_rate:.2f}"


