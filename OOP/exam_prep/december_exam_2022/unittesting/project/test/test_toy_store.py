from unittest import TestCase, main

from project.toy_store import ToyStore

class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.test_store = ToyStore()

    def test_correct_initialization(self):
        res = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, res)

    def test_add_toy_with_incorrect_shelf_raises_exception(self):
        res = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, res)

        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy("H", "pistol")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(self.test_store.toy_shelf, res)

    def test_add_toy_with_same_name_raises_exception(self):
        self.test_store.add_toy("A", "test")
        res = {
            "A": "test",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, res)

        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy("A", "test")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual(self.test_store.toy_shelf, res)

    def test_add_toy_on_taken_shelf_raises_exception(self):
        self.test_store.add_toy("A", "test")

        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy("A", "test2")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        shop = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, shop)
        res = self.test_store.add_toy("A", "test")
        self.assertEqual("Toy:test placed successfully!", res)
        updated_shop = {
            "A": "test",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, updated_shop)

    def test_remove_toy_with_wrong_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.remove_toy("H", "test")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_with_wrong_toy(self):
        self.test_store.add_toy("A", "test")
        shop = {
            "A": "test",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, shop)

        with self.assertRaises(Exception) as ex:
            self.test_store.remove_toy("A", "asd")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.test_store.add_toy("A", "test")
        shop = {
            "A": "test",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        res = self.test_store.remove_toy("A", "test")
        self.assertEqual("Remove toy:test successfully!", res)

        u_shop = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.test_store.toy_shelf, u_shop)

if __name__ == "__main__":
    main()