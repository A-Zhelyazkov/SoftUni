from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        else:
            computer = Laptop(manufacturer, model)

        build = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return build

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for pc in self.warehouse:
            if pc.price <= client_budget and pc.processor == wanted_processor and pc.ram >= wanted_ram:
                self.warehouse.remove(pc)
                self.profits += client_budget - pc.price
                return f"{pc} sold for {client_budget}$."
        else:
            raise Exception(f"Sorry, we don't have a computer for you.")

