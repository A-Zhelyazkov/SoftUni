from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
            return product
        except StopIteration:
            pass

    def remove(self, product_name):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
            self.products.remove(product)
        except StopIteration:
            pass

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f"{product}: {product.quantity}\n"

        return result[:-1]