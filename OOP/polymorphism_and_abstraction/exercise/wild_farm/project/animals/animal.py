from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def food_like(self):
        pass

    def feed(self, food):
        if type(food) not in self.food_like:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.get_weight()
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, " \
               f"{self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, " \
               f"{self.living_region}, {self.food_eaten}]"