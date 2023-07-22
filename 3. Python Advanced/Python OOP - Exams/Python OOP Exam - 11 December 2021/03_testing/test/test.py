from project.team import Team
from unittest import TestCase


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team('Random')

    def test_initialization(self):
        self.assertEqual('Random', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_raise_error_value_not_alpha(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'Random1'

        self.assertEqual(f"Team Name can contain only letters!", str(ve.exception))

    def test_add_member_method(self):
        self.team.members = {'first': 20, 'second': 17}

        result = self.team.add_member(second=15, third=18, forth=21)

        self.assertEqual({'first': 20, 'second': 17, 'third': 18, 'forth': 21}, self.team.members)
        self.assertEqual(f"Successfully added: third, forth", result)

    def test_remove_member_name_in_members(self):
        self.team.members = {'first': 20, 'second': 17, 'third': 18}

        result = self.team.remove_member('first')

        self.assertEqual({'second': 17, 'third': 18}, self.team.members)
        self.assertEqual(f"Member first removed", result)

    def test_remove_member_name_not_in_members(self):
        self.team.members = {'first': 20, 'second': 17, 'third': 18}

        result = self.team.remove_member('forth')

        self.assertEqual({'first': 20, 'second': 17, 'third': 18}, self.team.members)
        self.assertEqual(f"Member with name forth does not exist", result)

    def test_gt_method_return_true(self):
        self.team.members = {'first': 20, 'second': 17, 'third': 18}
        other = Team('Randommmmmm')
        other.members = {'first1': 24, 'second2': 19}

        result = self.team.__gt__(other)

        self.assertEqual(True, result)

    def test_gt_method_return_false(self):
        self.team.members = {'first': 20, 'second': 17}
        other = Team('Randommmmmm')
        other.members = {'first1': 24, 'second2': 19, 'third': 28}

        result = self.team.__gt__(other)

        self.assertEqual(False, result)

    def test_len_method(self):
        self.team.members = {'first': 20, 'second': 17, 'third': 18}

        result = self.team.__len__()

        self.assertEqual(3, result)

    def test_add_method(self):
        other = Team('Randommmmmm')

        self.team.members = {'a': 20, 'b': 18}
        other.members = {'c': 30, 'd': 16, 'e': 19}

        new_team = self.team.__add__(other)

        self.assertEqual('RandomRandommmmmm', new_team.name)
        self.assertEqual({'a': 20, 'b': 18, 'c': 30, 'd': 16, 'e': 19}, new_team.members)

    def test_str_method(self):
        self.team.members = {'a': 24, 'b': 19, 'd': 28, 'c': 28,  'e': 17, 'f': 18}

        result = str(self.team)

        expected = f"Team name: Random\n" \
                   f"Member: c - 28-years old\n" \
                   f"Member: d - 28-years old\n" \
                   f"Member: a - 24-years old\n" \
                   f"Member: b - 19-years old\n" \
                   f"Member: f - 18-years old\n" \
                   f"Member: e - 17-years old"

        self.assertEqual(expected, result)

