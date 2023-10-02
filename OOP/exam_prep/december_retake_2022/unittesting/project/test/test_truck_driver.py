from unittest import TestCase, main

from project.truck_driver import TruckDriver

class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("test", 10)

    def test_correct_initialization(self):
        self.assertEqual(self.driver.name, "test")
        self.assertEqual(self.driver.money_per_mile, 10)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_setter_earned_money_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual("test went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_with_same_offer_raises_exception(self):
        self.assertEqual(self.driver.available_cargos, {})

        result = self.driver.add_cargo_offer("BG", 100)
        self.assertEqual("Cargo for 100 to BG was added as an offer.", result)
        self.assertEqual(self.driver.available_cargos, {"BG": 100})

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("BG", 150)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.assertEqual(self.driver.available_cargos, {"BG": 100})

    def test_drive_best_cargo_offer_without_offers(self):
        self.assertEqual(self.driver.available_cargos, {})
        res = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", res)

    def test_drive_best_cargo_with_multiple_offers(self):
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)
        self.assertEqual(self.driver.available_cargos, {})
        self.driver.add_cargo_offer("BG", 100)
        self.assertEqual(self.driver.available_cargos, {"BG": 100})

        self.driver.add_cargo_offer("RO", 150)
        self.assertEqual(self.driver.available_cargos, {"BG": 100, "RO": 150})

        self.driver.add_cargo_offer("TR", 200)
        self.assertEqual(self.driver.available_cargos, {"BG": 100, "RO": 150, "TR": 200})

        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("test is driving 200 to TR.", result)

        self.assertEqual(self.driver.earned_money, 2000)
        self.assertEqual(self.driver.miles, 200)
        self.assertIsNone(self.driver.check_for_activities(200))

        self.driver.add_cargo_offer("GE", 240)
        result2 = self.driver.drive_best_cargo_offer()
        self.assertEqual("test is driving 240 to GE.", result2)
        self.assertEqual(self.driver.earned_money, 4400)
        self.assertEqual(self.driver.miles, 440)

    def test_check_for_activities(self):
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.add_cargo_offer("USA", 10000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 88250)
        self.assertEqual(self.driver.miles, 10000)

    def test__repr__method_with_no_miles(self):
        res = self.driver.__repr__()
        self.assertEqual("test has 0 miles behind his back.", res)

    def test__repr__method_with_miles(self):
        self.driver.miles = 10
        res = self.driver.__repr__()
        self.assertEqual("test has 10 miles behind his back.", res)


if __name__ == "__main__":
    main()