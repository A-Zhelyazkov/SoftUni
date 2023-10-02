from project.booths.booth import Booth


class OpenBooth(Booth):
    OPEN_BOOTH_PRICE = 2.5

    def reserve(self, number_of_people):
        price = self.OPEN_BOOTH_PRICE * number_of_people
        self.price_for_reservation = price
        self.is_reserved = True
