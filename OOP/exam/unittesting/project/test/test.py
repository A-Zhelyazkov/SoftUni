from unittest import TestCase, main

from project.second_hand_car import SecondHandCar

class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.test_car = SecondHandCar("M5", "sedan", 50000, 10000)

    def test_correct_initializations(self):
        self.assertEqual(self.test_car.model, "M5")
        self.assertEqual(self.test_car.car_type, "sedan")
        self.assertEqual(self.test_car.mileage, 50000)
        self.assertEqual(self.test_car.price, 10000)
        self.assertEqual(self.test_car.repairs, [])

    def test_price_setter_with_one_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car.price = 1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_mileage_setter_with_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car.mileage = 100

        result = "Please, second-hand cars only! Mileage must be greater than 100!"
        self.assertEqual(result, str(ve.exception))

    def test_set_promotional_price_with_higher_value_raises_error(self):
        self.assertEqual(self.test_car.price, 10000)
        with self.assertRaises(ValueError) as ve:
            self.test_car.set_promotional_price(10001)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))
        self.assertEqual(self.test_car.price, 10000)

    def test_set_promotional_price_with_lesser_value_sets_price(self):
        self.assertEqual(self.test_car.price, 10000)
        res = self.test_car.set_promotional_price(9000)
        self.assertEqual(res, "The promotional price has been successfully set.")
        self.assertEqual(self.test_car.price, 9000)

    def test_need_repair_with_high_price(self):
        self.assertEqual(self.test_car.repairs, [])
        res = self.test_car.need_repair(6000, "engine")
        self.assertEqual("Repair is impossible!", res)
        self.assertEqual(self.test_car.repairs, [])

    def test_need_repair_with_correct_value(self):
        self.assertEqual(self.test_car.repairs, [])
        self.assertEqual(self.test_car.price, 10000)
        res = self.test_car.need_repair(2000, "engine")
        self.assertEqual("Price has been increased due to repair charges.", res)
        self.assertEqual(self.test_car.repairs, ["engine"])
        self.assertEqual(self.test_car.price, 12000)

    def test_greater_than_method(self):
        car2 = SecondHandCar("M3", "coupe", 20000, 9000)
        res = self.test_car > car2
        self.assertEqual("Cars cannot be compared. Type mismatch!", res)
        car2.car_type = "sedan"
        res2 = self.test_car > car2
        self.assertTrue(res2)

    def test__str__method(self):
        res = f"""Model {self.test_car.model} | Type {self.test_car.car_type} | Milage {self.test_car.mileage}km
Current price: {self.test_car.price:.2f} | Number of Repairs: {len(self.test_car.repairs)}"""
        self.assertEqual(res, str(self.test_car))



if __name__ == "__main__":
    main()