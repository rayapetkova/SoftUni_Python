from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Lolly", "Cat", "Meow")

    def test_initialization(self):
        self.assertEqual("Lolly", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        self.assertEqual(f"Lolly makes Meow", self.mammal.make_sound())

    def test_get_kingdom_method(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method(self):
        self.assertEqual(f"Lolly is of type Cat", self.mammal.info())


if __name__ == "__main__":
    main()