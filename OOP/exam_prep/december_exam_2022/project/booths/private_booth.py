from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRIVATE_BOOTH_PRICE = 3.5

    def reserve(self, number_of_people):
        price = self.PRIVATE_BOOTH_PRICE * number_of_people
        self.is_reserved = True
        self.price_for_reservation = price
