from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTests(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Random', 20, 100)

    def test_initialization(self):
        self.assertEqual('Random', self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_raise_value_error_value_less_than_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Ra'

        self.assertEqual(f"Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_raise_value_error_value_less_than_eighteen(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual(f"Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_tournament_name_not_in_wins(self):
        self.player.wins = ['first', 'second', 'third']

        self.player.add_new_win('forth')

        self.assertEqual(['first', 'second', 'third', 'forth'], self.player.wins)

    def test_add_new_win_tournament_name_in_wins(self):
        self.player.wins = ['first', 'second', 'third']

        result = self.player.add_new_win('first')

        self.assertEqual(f"first has been already added to the list of wins!", result)

    def test__lt__method_self_points_less_than_other_points(self):
        other = TennisPlayer('Player2', 30, 120)

        result = self.player.__lt__(other)

        self.assertEqual(f"Player2 is a top seeded player and he/she is better than Random", result)

    def test__lt__method_self_points_more_than_other_points(self):
        other = TennisPlayer('Player2', 30, 50)

        result = self.player.__lt__(other)

        self.assertEqual(f"Random is a better player than Player2", result)

    def test__str__method(self):
        self.player.wins = ['first', 'second', 'third']

        self.assertEqual(f"Tennis Player: Random\n"
                         f"Age: 20\n"
                         f"Points: 100.0\n"
                         f"Tournaments won: first, second, third",
                         str(self.player))


if __name__ == "__main__":
    main()
