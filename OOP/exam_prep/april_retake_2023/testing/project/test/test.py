from unittest import TestCase, main
from project.robot import Robot

class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1", "Military", 10, 100)

    def test_class_attributes(self):

        self.assertEqual(["Military", "Education", "Entertainment", "Humanoids"], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_wrong_category_getter_and_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Battle"
        self.assertEqual(f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_set_negative_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_existing_hardware_component_doesnt_work(self):
        self.robot.hardware_upgrades.append("Test")
        self.assertEqual(1, len(self.robot.hardware_upgrades))
        self.assertEqual(100, self.robot.price)
        result = self.robot.upgrade("Test", 1)
        self.assertEqual(f"Robot {'1'} was not upgraded.", result)
        self.assertEqual(1, len(self.robot.hardware_upgrades))
        self.assertEqual(100, self.robot.price)

    def test_upgrade_with_correct_details(self):
        self.robot.hardware_upgrades.append("Test")
        self.assertEqual(1, len(self.robot.hardware_upgrades))
        result = self.robot.upgrade("Test2", 1)
        self.assertEqual(f"Robot {'1'} was upgraded with Test2.", result)
        self.assertEqual(2, len(self.robot.hardware_upgrades))
        self.assertEqual(101.5, self.robot.price)


    def test_update_with_lower_version(self):
        self.robot.software_updates.append(3)
        self.assertEqual(1, len(self.robot.software_updates))
        result = self.robot.update(1, 1)
        self.assertEqual("Robot 1 was not updated.", result)
        self.assertEqual(1, len(self.robot.software_updates))

    def test_update_with_not_enough_capacity(self):
        self.robot.available_capacity = 2
        self.robot.software_updates.append(3)
        self.assertEqual(1, len(self.robot.software_updates))
        result = self.robot.update(5, 3)
        self.assertEqual("Robot 1 was not updated.", result)
        self.assertEqual(1, len(self.robot.software_updates))

    def test_update_with_higher_version_and_enough_capacity(self):
        self.robot.software_updates.append(3)
        self.assertEqual(1, len(self.robot.software_updates))
        self.assertEqual(10, self.robot.available_capacity)
        result = self.robot.update(5, 2)
        self.assertEqual("Robot 1 was updated to version 5.", result)
        self.assertEqual(2, len(self.robot.software_updates))
        self.assertEqual(8, self.robot.available_capacity)

    def test_gt_method(self):
        robot2 = Robot("2", "Military", 5, 50)
        robot3 = Robot("3", "Military", 5, 150)
        result = self.robot > robot2
        self.assertEqual("Robot with ID 1 is more expensive than Robot with ID 2.", result)
        result2 = self.robot > robot3
        self.assertEqual("Robot with ID 1 is cheaper than Robot with ID 3.", result2)


    def test_equal_prices(self):
        robot2 = Robot("2", "Military", 5, 100)
        result = self.robot > robot2
        self.assertEqual('Robot with ID 1 costs equal to Robot with ID 2.', result)
if __name__ == "__main__":
    main()

