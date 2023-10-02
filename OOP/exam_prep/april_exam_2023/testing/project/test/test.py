from unittest import TestCase, main

from project.tennis_player import TennisPlayer

class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.test = TennisPlayer("test", 20, 50)

    def test_correct_initializing(self):
        self.assertEqual("test", self.test.name)
        self.assertEqual(20, self.test.age)
        self.assertEqual(50, self.test.points)
        self.assertEqual([], self.test.wins)

    def test_name_setter_with_wrong_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.name = "t"
        res = "Name should be more than 2 symbols!"
        self.assertEqual(res, str(ve.exception))

    def test_age_setter_with_below_18_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.age = 17
        res = "Players must be at least 18 years of age!"
        self.assertEqual(res, str(ve.exception))

    def test_add_new_win_with_same_tournament_should_not_add(self):
        self.test.add_new_win("BG")
        self.assertEqual(1, len(self.test.wins))
        self.assertEqual(["BG"], self.test.wins)

        result = self.test.add_new_win("BG")
        self.assertEqual("BG has been already added to the list of wins!", result)
        self.assertEqual(1, len(self.test.wins))
        self.assertEqual(["BG"], self.test.wins)

    def test_add_new_win_with_correct_data_should_add(self):
        self.test.add_new_win("BG")
        self.assertEqual(1, len(self.test.wins))
        self.assertEqual(["BG"], self.test.wins)

        result = self.test.add_new_win("ENG")
        self.assertIsNone(result)
        self.assertEqual(["BG", "ENG"], self.test.wins)
        self.assertEqual(2, len(self.test.wins))

    def test_lt_method(self):
        test2 = TennisPlayer("test2", 20, 60)
        res = self.test < test2
        self.assertEqual("test2 is a top seeded player and he/she is better than test", res)
        self.test.points = 100
        res2 = self.test < test2
        self.assertEqual("test is a better player than test2", res2)

    def test_str_method_with_one_win(self):
        self.test.add_new_win("BG")
        res = f"Tennis Player: test\n" \
               f"Age: 20\n" \
               f"Points: 50.0\n" \
               f"Tournaments won: BG"
        self.assertEqual(self.test.__str__(), res)

    def test_str_no_wins(self):
        result = f"Tennis Player: test\n" \
               f"Age: 20\n" \
               f"Points: 50.0\n" \
               f"Tournaments won: "

        self.assertEqual(str(self.test), result)

    def test_str_with_more_wins(self):
        self.test.wins = ["BG", "ENG"]
        result = f"Tennis Player: test\n" \
               f"Age: 20\n" \
               f"Points: 50.0\n" \
               f"Tournaments won: BG, ENG"
        self.assertEqual(str(self.test), result)


if __name__ == "__main__":
    main()