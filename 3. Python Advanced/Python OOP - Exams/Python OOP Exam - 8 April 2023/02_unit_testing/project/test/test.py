from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTests(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("TestName", 23, 100)
        self.other = TennisPlayer("Second", 30, 200)

    def test_initialization(self):
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(23, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

        self.assertEqual("Second", self.other.name)
        self.assertEqual(30, self.other.age)
        self.assertEqual(200, self.other.points)
        self.assertEqual([], self.other.wins)

    def test_name_setter_raise_error_name_less_or_equal_to_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "ka"

        self.assertEqual(f"Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_raise_error_age_less_than_eighteen(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 16

        self.assertEqual(f"Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_method_tournament_name_not_in_wins(self):
        self.player.add_new_win("Random")

        self.assertEqual(["Random"], self.player.wins)

    def test_add_new_win_method_tournament_name_in_wins(self):
        self.player.wins = ["Random"]

        result = self.player.add_new_win("Random")

        self.assertEqual(f"Random has been already added to the list of wins!", result)

    def test_lt_method_point_less_than_other_points(self):
        result = self.player.__lt__(self.other)

        self.assertEqual(f"{self.other.name} is a top seeded player and he/she is better than {self.player.name}", result)

    def test_lt_method_poin_greater_or_equal_to_other_points(self):
        self.other.points = 80

        result = self.player.__lt__(self.other)

        self.assertEqual(f"{self.player.name} is a better player than {self.other.name}", result)

    def test_str_method(self):
        self.player.wins = ["Random1", "Random2"]

        result = str(self.player)

        self.assertEqual(f"Tennis Player: TestName\n"
                         f"Age: 23\n"
                         f"Points: 100.0\n"
                         f"Tournaments won: Random1, Random2", result)


if __name__ == "__main__":
    main()
