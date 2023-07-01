from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("First", 12, 50, 70)
        self.enemy_hero = Hero("Second", 10, 60, 40)

    def test_battle_method_raise_exception_if_hero_name_and_enemy_hero_name_are_equal(self):
        self.enemy_hero.username = "First"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight yourself", str(ex.exception))

    def test_battle_method_raise_error_if_hero_health_is_zero_or_negative(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_method_raise_error_if_enemy_hero_health_is_zero_or_negative(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight Second. He needs to rest", str(ve.exception))

    def test_battle_method_with_hero_and_enemy_hero_health_zero_or_negative(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 100

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", result)

    def test_battle_method_with_hero_health_greater_than_zero_and_enemy_health_zero_or_negative(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 1

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(13, self.hero.level)
        self.assertEqual(45, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_with_hero_health_zero_or_negative_and_enemy_health_greater_than_zero(self):
        self.hero.damage = 1
        self.enemy_hero.damage = 100

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(53, self.enemy_hero.health)
        self.assertEqual(105, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        self.assertEqual(f"Hero First: 12 lvl\nHealth: 50\nDamage: 70\n", str(self.hero))


if __name__ == "__main__":
    main()
