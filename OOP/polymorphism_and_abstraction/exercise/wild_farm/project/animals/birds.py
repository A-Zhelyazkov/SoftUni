from project.animals.animal import Bird
from project.food import Meat, Fruit, Seed, Vegetable


class Owl(Bird):
    def get_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_like(self):
        return [Meat]


class Hen(Bird):
    def get_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"

    @property
    def food_like(self):
        return [Fruit, Meat, Seed, Vegetable]