from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def get_weight(self):
        return 0.1

    def make_sound(self):
        return "Squeak"

    @property
    def food_like(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    def get_weight(self):
        return 0.4

    def make_sound(self):
        return "Woof!"

    @property
    def food_like(self):
        return [Meat]


class Cat(Mammal):
    def get_weight(self):
        return 0.3

    def make_sound(self):
        return "Meow"

    @property
    def food_like(self):
        return [Vegetable, Meat]


class Tiger(Mammal):
    def get_weight(self):
        return 1

    def make_sound(self):
        return "ROAR!!!"

    @property
    def food_like(self):
        return [Meat]