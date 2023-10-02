from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def type_pc(self):
        pass

    @property
    @abstractmethod
    def processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @staticmethod
    def power_of_two(num):
        return log2(num)

    def configure_computer(self, processor, ram):
        if processor not in self.processors:
            raise ValueError(f"{processor} is not compatible with {self.type_pc} {self.__manufacturer} "
                             f"{self.__model}!")

        if not self.power_of_two(ram).is_integer() or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type_pc} {self.__manufacturer} "
                             f"{self.__model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.processors[processor]
        self.price += int(self.power_of_two(ram) * 100)

        return f"Created {self.__manufacturer} {self.__model} with {processor} and {ram}GB RAM " \
               f"for {self.price}$."

    def __repr__(self):
        return  f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"