from project.clients.base_client import BaseClient


class Student(BaseClient):

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, 2)

    def increase_clients_interest(self): #TODO percantage might not be added
        self.interest += 1
