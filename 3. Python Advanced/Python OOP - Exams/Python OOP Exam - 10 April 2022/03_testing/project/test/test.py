from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Random', 2000, 10)

    def test_initialization(self):
        self.assertEqual('Random', self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raise_error_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual(f"Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_raise_error_year_is_less_than_needed(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual(f"Year is not valid!", str(ve.exception))

    def test_add_actor_name_already_in_actors(self):
        self.movie.actors = ['first', 'second', 'third']

        result = self.movie.add_actor('first')
        self.assertEqual(f"first is already added in the list of actors!", result)

    def test_add_actor_method_actor_not_in_actors(self):
        self.movie.actors = ['first', 'second', 'third']

        self.movie.add_actor('forth')

        self.assertEqual(['first', 'second', 'third', 'forth'], self.movie.actors)

    def test_gt_method_self_rating_greater_than_other_rating(self):
        other = Movie('Random2', 2001, 9)

        result = self.movie.__gt__(other)

        self.assertEqual(f'"Random" is better than "Random2"', result)

    def test_gt_method_self_rating_less_than_other_rating(self):
        other = Movie('Random2', 2001, 11)

        result = self.movie.__gt__(other)

        self.assertEqual(f'"Random2" is better than "Random"', result)

    def test_gt_method_self_rating_equal_to_other_rating(self):
        other = Movie('Random2', 2001, 10)

        result = self.movie.__gt__(other)

        self.assertEqual(f'"Random2" is better than "Random"', result)

    def test_repr_method(self):
        self.movie.actors = ['Random', 'Random3', 'Random4']
        expected = f"Name: Random\nYear of Release: 2000\nRating: 10.00\n" \
                   f"Cast: Random, Random3, Random4"

        self.assertEqual(expected, self.movie.__repr__())


if __name__ == '__main__':
    main()
